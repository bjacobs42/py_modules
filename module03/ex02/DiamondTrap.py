from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Represents a certain king of the Baratheon family,
    inheriting from the class Baratheon and Lannister.

    Attributes:
        first_name (str): The first name of the Baratheon character.
        is_alive (bool): Indicates if the character is alive. Default is True.
        family_name (str): The family_name of Baratheon. Always is Baratheon.
        hairs (str): Hair type of the character. Default is dark.
        eyes (str): Eye color of the character. Default is brown.
    """

    def __init__(
        self,
        first_name: str,
        is_alive: bool = True,
        eyes: str = "brown",
        hairs: str = "dark"
    ):
        """
        Initializes a King instance with a first name,
        alive status, and family details.
        """
        Baratheon.__init__(self, first_name, is_alive, eyes, hairs)

    @property
    def get_eyes(self) -> str:
        return (self.eyes)

    @property
    def get_hairs(self) -> str:
        return (self.hairs)

    @get_hairs.setter
    def set_hairs(self, new_hairs: str) -> None:
        self.hairs = new_hairs

    @get_eyes.setter
    def set_eyes(self, new_eyes: str) -> None:
        self.eyes = new_eyes
