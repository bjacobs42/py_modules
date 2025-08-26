def square(number: int | float) -> int | float:
    return (number ** 2)

def pow(number: int | float) -> int | float:
    return(number ** number)

def outer(number: int | float, function) -> object:
    def inner() -> float:
        nonlocal number
        number = function(number)
        return (number)

    return (inner)
