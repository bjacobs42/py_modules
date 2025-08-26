def slice_me(family: list, start: int, end: int) -> list:
    """
    Returns a sliced portion of the `family` list from the `start` index up to-
    but not including, the `end` index.

    ValueError when start is bigger than the length of `family`,
    when `family` is not a list or when family array's length != 2.
    """

    if not isinstance(family, list):
        raise ValueError("family should be a list")
    if not all(len(v2) == 2
               and isinstance(v2, (list, tuple)) for v2 in family):
        raise ValueError("family vector should be 2d")
    family_len = len(family)
    if start > family_len:
        raise ValueError("start is bigger than list")
    if end > family_len:
        end = family_len

    print(f"My shape is : ({family_len}, 2)")
    new_family: list = family[slice(start, end)]
    print(f"My new shape is : ({len(new_family)}, 2)")
    return new_family
