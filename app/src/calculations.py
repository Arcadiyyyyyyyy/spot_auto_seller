def is_more_than_min_order(symbol_info: dict):
    ticker = symbol_info.get("symbol")
    free_amount_of_coin = symbol_info.get("free")

    print(symbol_info)
