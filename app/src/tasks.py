import logging

from .binance_talker import BinanceGetInfoConnector, BinancePostInfoConnector


def sell_binance_tickers_that_are_in_the_env_list():
    info_about_spot_coins = BinanceGetInfoConnector().get_account_data()
    logging.info(f"Fetched info about spot coins. Found {len(info_about_spot_coins)} coins to sell")
    for coin_to_sell in info_about_spot_coins:
        BinancePostInfoConnector().sell_all_spot_coins_with_ticker(coin_to_sell)
        logging.info(f"Sold {coin_to_sell.get('symbol', '')}")
