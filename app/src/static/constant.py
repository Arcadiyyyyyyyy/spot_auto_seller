from enum import Enum


class MinimumToDisplay(Enum):
    minimum_asset_btc_cost = 0.00001


class Other(Enum):
    sell_order_multiplier = 0.99


class HowOftenToExecute(Enum):
    seconds_sell_if_enough_to_sell = 1
