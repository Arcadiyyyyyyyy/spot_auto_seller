import logging
import time
import schedule

from dotenv import load_dotenv
from traceback import format_exception

from src.regular_tasks import sell_if_enough_to_sell
from src.config import Settings, configure_logging
from src.binance_talker import BinanceGetInfoConnector


def main():
    load_dotenv()
    Settings()
    configure_logging()

    BinanceGetInfoConnector().check_if_api_key_is_valid()

    sell_if_enough_to_sell()

    logging.info("Started!")

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            logging.warning("Finished with Ctrl+C")
            return
        except Exception as e:
            logging.error(format_exception(e))


if __name__ == "__main__":
    main()
