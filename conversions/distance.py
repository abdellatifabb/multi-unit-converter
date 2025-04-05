"""
Module: distance.py
Provides functions for converting distances between kilometers and miles.
"""

def km_to_miles(km):
    """
    Convert kilometers to miles.

    Args:
        km (float or int): Distance in kilometers.

    Returns:
        float: Distance in miles.

    Raises:
        ValueError: If the input is not a numeric value.
    """
    try:
        km = float(km)
    except (ValueError, TypeError):
        raise ValueError("Input must be a numeric value.")
    return km * 0.621371