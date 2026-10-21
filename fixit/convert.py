"""Unit conversions."""

KM_PER_MILE = 1.609344


def celsius_to_fahrenheit(c: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Example:
        celsius_to_fahrenheit(0) returns 32.
    """
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius.

    Example:
        fahrenheit_to_celsius(32) returns 0.
    """
    return (f - 32) * 5 / 9


def km_to_miles(km: float) -> float:
    """Convert kilometers to miles.

    Example:
        km_to_miles(1) returns approximately 0.6214.
    """
    return km / KM_PER_MILE


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometers.

    Example:
        miles_to_km(1) returns approximately 1.6093.
    """
    return miles * KM_PER_MILE
