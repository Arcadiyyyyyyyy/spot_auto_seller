import logging
import time
import schedule

from dotenv import load_dotenv
from traceback import format_exception

from src.config import Settings, configure_logging
from src.binance_talker import BinanceGetInfoConnector
from src.tasks import notify_all_admins_in_telegram


def main():
    load_dotenv()
    Settings()
    configure_logging()

    BinanceGetInfoConnector().check_if_api_key_is_valid()

    logging.info("Started!")

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            logging.warning("Finished with Ctrl+C")
            return
        except Exception as e:
            notify_all_admins_in_telegram("Error happened in spot_auto_seller. Check the logs asap.")
            logging.error(format_exception(e))


if __name__ == "__main__":
    main()
