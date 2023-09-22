import logging

from dotenv import load_dotenv

from src.config import Settings, configure_logging
from src.tasks import sell_binance_tickers_that_are_in_the_env_list
from src.binance_talker import BinanceGetInfoConnector


def main():
    load_dotenv()
    Settings()
    configure_logging()

    BinanceGetInfoConnector().check_if_api_key_is_valid()

    logging.info("Started!")
    # TODO: scheduler run
    print(sell_binance_tickers_that_are_in_the_env_list())


if __name__ == "__main__":
    main()
