"""
Module: mass.py
Provides functions for converting mass between kilograms and pounds.
"""



def kg_to_lb(kg):
    """
    Convert kilograms to pounds.

    Args:
        kg (float): Mass in kilograms.

    Returns:
        float: Mass in pounds.
    """
    return kg * 2.20462

def lb_to_kg(lb):
    """
    Convert pounds to kilograms.

    Args:
        lb (float): Mass in pounds.

    Returns:
        float: Mass in kilograms.
    """
    return lb / 2.20462
