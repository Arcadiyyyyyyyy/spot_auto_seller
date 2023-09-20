import logging

from dotenv import load_dotenv

from src.config import Settings, configure_logging
from src.tasks import sell_binance_tickers_that_are_in_the_env_list


def main():
    load_dotenv()
    Settings()
    configure_logging()

    logging.info("Started!")
    print(sell_binance_tickers_that_are_in_the_env_list())


if __name__ == "__main__":
    main()
