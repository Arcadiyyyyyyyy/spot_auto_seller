from src.config import Settings, configure_logging
from dotenv import load_dotenv


def main():
    load_dotenv()
    Settings()

    configure_logging()


if __name__ == "__main__":
    main()
