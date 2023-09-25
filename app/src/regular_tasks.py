import schedule

from .static.constant import HowOftenToExecute
from .tasks import sell_binance_tickers_that_are_in_the_env_list


def sell_if_enough_to_sell():
    schedule.every(
        HowOftenToExecute.seconds_sell_if_enough_to_sell.value
    ).seconds.do(
        sell_binance_tickers_that_are_in_the_env_list
    )
