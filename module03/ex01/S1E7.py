from S1E9 import Character


class Baratheon(Character):
    """
    Represents a member of the Baratheon family,
    inheriting from the Character class.

    Attributes:
        first_name (str): The first name of the Baratheon character.
        is_alive (bool): Indicates if the character is alive. Default is True.
        family_name (str): The family_name of Baratheon. Always is Baratheon.
        hairs (str): Hair type of the character. Default is dark.
        eyes (str): Eye color of the character. Default is brown.
    """

    def __str__(self):
        """
        Returns a human-readable string representation of the object.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def __repr__(self):
        """
        Returns an unambiguous and developer-oriented
        string representation of the object.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def __init__(
        self,
        first_name: str,
        is_alive: bool = True,
        eyes: str = "brown",
        hairs: str = "dark"
    ):
        """
        Initializes a Baratheon instance with a first name and alive status.

        Args:
            first_name (str): The first name of the Baratheon character.
            is_alive (bool): Whether the character is alive. Defaults to True.
            eyes (str): Eye color of the character. Default is blue.
            hairs (str): Hair type of the character. Default is light.
        """
        self.first_name = first_name
        self.family_name = "Baratheon"
        self.is_alive = is_alive
        self.eyes = eyes
        self.hairs = hairs


class Lannister(Character):
    """
    Represents a member of the Lannister family,
    inheriting from the Character class.

    Attributes:
        first_name (str): The first name of the Lannister character.
        is_alive (bool): Indicates if the character is alive. Default is True.
        family_name (str): The family_name of Lannister. Always is Lannister.
        eyes (str): Eye color of the character. Default is blue.
        hairs (str): Hair type of the character. Default is light.
    """

    def __init__(
        self,
        first_name: str,
        is_alive: bool = True,
        eyes: str = "blue",
        hairs: str = "light"
    ):
        """
        Initializes a Lannister instance with a first name and alive status.

        Args:
            first_name (str): The first name of the Lannister character.
            is_alive (bool): Whether the character is alive. Defaults to True.
            eyes (str): Eye color of the character. Default is blue.
            hairs (str): Hair type of the character. Default is light.
        """
        self.first_name = first_name
        self.family_name = "Lannister"
        self.is_alive = is_alive
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """
        Returns a human-readable string representation of the object.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def __repr__(self):
        """
        Returns an unambiguous and developer-oriented
        string representation of the object.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    @staticmethod
    def create_lannister(
        first_name: str,
        is_alive: bool = None,
        eyes: str = None,
        hairs: str = None
    ):
        """
        Method to create a new Lannister instance.

        Args:
            first_name (str): The first name of the Lannister character.
            is_alive (bool): Whether the character is alive. Defaults to True.
            eyes (str): Eye color of the character. Default is blue.
            hairs (str): Hair type of the character. Default is light.

        Returns:
            Lannister: A new instance of the Lannister class.
        """
        return (Lannister(first_name, is_alive))
