"""
Module: temperature.py
Provides functions for converting temperatures between Celsius and Fahrenheit.
"""

def c_to_f(celsius):
    """
    Convert Celsius to Fahrenheit.

    Args:
        celsius (float or int): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.

    Raises:
        ValueError: If the input is not a numeric value.
    """
    try:
        celsius = float(celsius)
    except (ValueError, TypeError):
        raise ValueError("Input must be a numeric value.")
    return (celsius * 9/5) + 32