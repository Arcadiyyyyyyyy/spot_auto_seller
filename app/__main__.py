import logging

from dotenv import load_dotenv

from src.config import Settings, configure_logging
from src.binance_talker import BinanceGetInfoConnector


def main():
    load_dotenv()
    Settings()
    configure_logging()

    logging.info("Started!")


if __name__ == "__main__":
    main()
