import sys


class StringInfo:
    """
    StringInfo(string: str)

    Class containing the number of lowercase/uppercase letters,
    punctuation marks, digits and spaces in a string.
    """

    def __init__(self, string: str):
        """
        Initializes the StringInfo object with the provided string.
        Counts the number of lowercase/uppercase letters, punctuation marks,
        digits and spaces.
        """

        self.characters = len(string)
        self.punctuations = 0
        self.lower_cases = 0
        self.upper_cases = 0
        self.digits = 0
        self.spaces = 0

        for char in string:
            if char == '!':
                self.punctuations += 1
            elif char.islower():
                self.lower_cases += 1
            elif char.isupper():
                self.upper_cases += 1
            elif char.isdigit():
                self.digits += 1
            elif char.isspace():
                self.spaces += 1

    def __str__(self):
        """
        Returns a formatted string containing all the counts.
        """

        return (f"Total characters: {self.characters}\n"
                f"Lowercase letters: {self.lower_cases}\n"
                f"Uppercase letters: {self.upper_cases}\n"
                f"Punctuation marks: {self.punctuations}\n"
                f"Digits: {self.digits}\n"
                f"Spaces: {self.spaces}")


def prompt_input_text() -> str:
    """
    Prompts the user for a string, stops when a valid string is provided.
    Returns the user input string.
    """

    string = input("What is the text to count?\n")
    while not string:
        print("Input cannot be empty, please try again")
        string = input("What is the text to count?\n")
    return string


def main():
    argc: int = len(sys.argv)
    try:
        assert argc <= 2, "more than one argument provided"
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return 1

    if argc == 1 or not sys.argv[1]:
        string_info = StringInfo(prompt_input_text())
    else:
        string_info = StringInfo(sys.argv[1])

    print(string_info)


if __name__ == "__main__":
    main()
