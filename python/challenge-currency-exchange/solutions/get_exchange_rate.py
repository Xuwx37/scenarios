import json


def get_exchange_rate(source_currency, target_currency):
    with open("/home/labex/project/usd.json", "r") as f:
        exchange_rates = json.load(f)
    try:
        source_rate = exchange_rates[source_currency]["rate"]
    except:
        raise ValueError(f"Invalid source currency: {source_currency}")
    try:
        target_rate = exchange_rates[target_currency]["rate"]
    except:
        raise ValueError(f"Invalid target currency: {target_currency}")

    return target_rate / source_rate
