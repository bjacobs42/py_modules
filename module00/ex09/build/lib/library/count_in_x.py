from typing import TypeVar, List, Tuple

T = TypeVar('T')


def count_in_list(lst: List[T], value: T) -> int:
    return lst.count(value)


def count_in_tuple(tup: Tuple[T], value: T) -> int:
    return tup.count(value)
