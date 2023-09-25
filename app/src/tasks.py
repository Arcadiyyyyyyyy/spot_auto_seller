import json
import logging

from os import environ
from telebot import TeleBot

from .binance_talker import BinanceGetInfoConnector, BinancePostInfoConnector


def sell_binance_tickers_that_are_in_the_env_list():
    info_about_spot_coins = BinanceGetInfoConnector().get_account_data()
    logging.info(f"Fetched info about spot coins. Found {len(info_about_spot_coins)} coins to sell")
    for coin_to_sell in info_about_spot_coins:
        BinancePostInfoConnector().sell_all_spot_coins_with_ticker(coin_to_sell)
        logging.info(f"Sold {coin_to_sell.get('symbol', '')}")


def notify_all_admins_in_telegram(message: str):
    notification_bot_token = environ.get("TELEGRAM_BOT_ADMIN_NOTIFICATOR_TOKEN")
    admins_to_notify_string = environ.get("LIST_OF_ADMINS_TELEGRAM_IDS")

    if notification_bot_token is not None and admins_to_notify_string is not None:
        admins_to_notify: list[int] = json.loads(admins_to_notify_string)
        bot = TeleBot(notification_bot_token)
        for admin_tg_id in admins_to_notify:
            bot.send_message(admin_tg_id, message)
