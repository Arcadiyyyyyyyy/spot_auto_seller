from binance import Client
from os import environ

from .static.constant import MinimumToDisplay


def _create_connection() -> Client:
    api_public = environ.get("BINANCE_API_PUBLIC")
    api_secret = environ.get("BINANCE_API_SECRET")
    return Client(api_public, api_secret)


class BinanceGetInfoConnector:
    c = None

    def __init__(self):
        self.c = _create_connection()

    def get_account_data(self):
        tickers_for_search = self._get_spot_balance()
        tickers_for_search = self._clean_tickers_list(tickers_for_search)
        return self._get_tickers_price(tickers_for_search)

    def _get_spot_balance(self) -> list[dict]:
        assets_that_cost_more_than_x = []

        for asset in self.c.get_user_asset():
            free_amount_of_asset = float(asset.get("free"))
            asset_btc_valuation = float(asset.get("btcValuation"))

            if free_amount_of_asset > 0 and \
                    asset_btc_valuation > MinimumToDisplay.minimum_asset_btc_cost.value:
                assets_that_cost_more_than_x.append(asset)

        return assets_that_cost_more_than_x

    def _clean_tickers_list(self, tickers_list: list[dict]):
        spot_pairs = [x.get("symbol") for x in self.c.get_exchange_info().get("symbols")]
        return [x for x in tickers_list if f"{x.get('symbol', '')}USDT" in spot_pairs]

    def _get_tickers_price(self, tickers_to_search: list[dict]):
        result_pairs = []
        pairs_to_search = [f"{x.get('asset')}USDT" for x in tickers_to_search]

        for symbol, deposit_info in zip(pairs_to_search, tickers_to_search):
            ticker = self.c.get_ticker(symbol=symbol)
            result_pairs.append({**ticker, **deposit_info})

        return result_pairs


class BinancePostInfoConnector:
    c = None

    def __init__(self):
        self.c = _create_connection()

    def sell_all_spot_coins_with_ticker(self, ticker):
        raise NotImplementedError
        self.c.order_market()
