from typing import Callable, Iterable, Iterator, Optional, TypeVar


def ft_filter(
    func: Optional[Callable[TypeVar('T'), bool]],
    iterable: Iterable[TypeVar('T')]
) -> Iterator[TypeVar('T')]:
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true.
    """
    if not func:
        items = [item for item in iterable if item]
    else:
        items = [item for item in iterable if func(item)]

    return items
