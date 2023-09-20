def is_more_than_min_order(symbol_info: dict):
    ticker = symbol_info.get("symbol")
    free_amount_of_coin = float(symbol_info.get("free"))
    single_coin_last_price = float(symbol_info.get("lastPrice"))

    for x in symbol_info.get("filters"):
        if x.get("filterType") == "NOTIONAL":
            minimum_usdt_amount_of_coin_to_sell = float(x.get("minNotional"))
            free_coins_usdt_price = free_amount_of_coin * single_coin_last_price

            if minimum_usdt_amount_of_coin_to_sell <= free_coins_usdt_price:
                return {
                    "is_more_than_min_order": True,
                    "symbol": ticker,
                    "available_to_sell_usdt": free_coins_usdt_price,
                    "available_to_sell_coin": free_amount_of_coin,
                    "minimum_usdt_order_size": minimum_usdt_amount_of_coin_to_sell
                }

    return {
        "is_more_than_min_order": False,
        "symbol": ticker,
    }
