import json


def get_exchange_rate(source_currency, target_currency):
    """
    Calculate the exchange rate between the two currencies.

    Args:
    original_currency (str): The three-letter currency code for the original currency.
    target_currency (str): The three-letter currency code for the target currency.

    Returns:
    exchange_rate(float): Return the exchange rate as a float.
    """
    with open("/home/labex/project/usd.json", "r") as f:
        exchange_rates = json.load(f)
    try:
        source_rate = exchange_rates[source_currency]["rate"]
    except:
        raise ValueError("Original currency code not supported")
    try:
        target_rate = exchange_rates[target_currency]["rate"]
    except:
        raise ValueError("Target currency code not supported")
    
    exchange_rate = target_rate / source_rate
    return exchange_rate
