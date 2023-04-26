# Get Exchange Rate

## Introduction

Your task is to create a function in `get_exchange_rate.py` that retrieves the exchange rate between two currencies. The function should take two arguments: the original currency code and the target currency code. The function should use an exchange rate API to get the exchange rate between the two currencies.

## Requirements

1. The function should be named `get_exchange_rate`.
2. The function should take two arguments: `original_currency` (string) and `target_currency` (string).
3. The function should use an exchange rate API to get the exchange rate between the two currencies.
4. The function should return the exchange rate as a float.
5. If the original currency code or the target currency code is invalid or not supported by the exchange rate API, the function should raise a `ValueError` exception with an appropriate error message.

## Examples

```python
>>> get_exchange_rate("eur", "gbp")
0.885
>>> get_exchange_rate("eur", "cny")
7.614
>>> get_exchange_rate("ABC", "eur")
ValueError: Original currency code not supported
>>> get_exchange_rate("eur", "XYZ")
ValueError: Target currency code not supported
```

The json file returns exchange rates in relation to the USD, so the function first retrieves the latest exchange rates from the json file and then calculates the exchange rate between the source and target currencies based on the USD exchange rates. If either the source or target currency is invalid, the function raises a ValueError.

- The exchange rate is the rates of `target_rate` divide the rates of `source_rate`.
