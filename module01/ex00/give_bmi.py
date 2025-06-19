def is_float_or_int(value: any) -> bool:
    """
    Uses isinstance to check if a value is an int or a float.
    Returns false if value is not an int or a float.
    """
    return isinstance(value, (int, float))


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    Calculates bmi value from a list of heights and weights.

    Throws ValueError if heights and lists length don't match
    or when a value is not an int or float.

    Returns a list of bmi values.
    """

    if len(height) != len(weight):
        raise ValueError("height and weight are not of equal length")

    bmi: list[int | float] = []
    for metre, kg in zip(height, weight):
        if not is_float_or_int(metre):
            raise ValueError(f"{metre} is not an int or float")
        if not is_float_or_int(kg):
            raise ValueError(f"{kg} is not an int or float")
        bmi.append(kg / (metre * metre))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks bmi values from a list of bmi values and returns a list of bool,
    true if bmi value exceeds limit otherwise false.

    Ignores values which are not int or float
    """

    limit_passed: list = [value > limit
                          for value in bmi
                          if is_float_or_int(value)]
    return limit_passed
