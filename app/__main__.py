from src.config import Settings, configure_logging
from dotenv import load_dotenv
from src.binance_talker import BinanceConnector


def main():
    load_dotenv()
    Settings()
    configure_logging()

    print(BinanceConnector().get_account_data())


if __name__ == "__main__":
    main()
