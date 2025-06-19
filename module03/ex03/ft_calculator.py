class calculator:
    """
    A class that holds a list of numbers and allows modification
    by using operators.
    """

    def __init__(self, numbers=None):
        if numbers is None:
            numbers = []
        self._numbers = numbers

    def __add__(self, num) -> None:
        """Increases each number in the container by the given value."""
        if not isinstance(num, (int, float, complex)):
            return NotImplemented

        self._numbers = [x + num for x in self._numbers]
        print(f"after addition: {self._numbers}")

    def __sub__(self, num) -> None:
        """Subtracts each number in the container by the given value."""
        if not isinstance(num, (int, float, complex)):
            return NotImplemented

        self._numbers = [x - num for x in self._numbers]
        print(f"after subtraction: {self._numbers}")

    def __mul__(self, num) -> None:
        """Multiplies each number in the container by the given value."""
        if not isinstance(num, (int, float, complex)):
            return NotImplemented

        self._numbers = [x * num for x in self._numbers]
        print(f"after multiplication: {self._numbers}")

    def __truediv__(self, num) -> None:
        """Divides(truediv) each number in the container by the given value."""
        if not isinstance(num, (int, float, complex)):
            return NotImplemented
        if num == 0:
            return ValueError("Cannot divide by 0")

        self._numbers = [x / num for x in self._numbers]
        print(f"after division: {self._numbers}")
