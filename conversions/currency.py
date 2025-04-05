"""
Module: currency.py
Provides functions for converting currency between EUR and USD using a fixed exchange rate.
"""

# Example fixed exchange rates:
EUR_TO_USD_RATE = 1.1  # 1 EUR = 1.1 USD
USD_TO_EUR_RATE = 1 / EUR_TO_USD_RATE  # Approximately 0.90909 EUR per 1 USD

def eur_to_usd(eur):
    """
    Convert Euros to US Dollars.

    Args:
        eur (float or int): Amount in Euros.

    Returns:
        float: Equivalent amount in US Dollars.

    Raises:
        ValueError: If the input is not a numeric value.
    """
    try:
        eur = float(eur)
    except (ValueError, TypeError):
        raise ValueError("Input must be a numeric value.")
    return eur * EUR_TO_USD_RATE