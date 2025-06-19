from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class representing a character with basic attributes
    and behaviors.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): Indicates if the character is alive. Default is True.
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Abstract method to initializes a Character instance.
        """
        pass

    def die(self) -> None:
        """
        Marks the character as dead by setting the `is_alive` attribute to False.
        """
        self.is_alive = False


class Stark(Character):
    """
    Represents a member of the Stark family, inheriting from the Character class.

    Attributes:
        first_name (str): The first name of the Stark character.
        is_alive (bool): Indicates if the character is alive. Default is True.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initializes a Stark instance with a first name and alive status.

        Args:
            first_name (str): The first name of the Stark character.
            is_alive (bool): Whether the character is alive. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive
