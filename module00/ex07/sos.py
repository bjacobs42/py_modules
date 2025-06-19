import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def main():
    try:
        argc = len(sys.argv)
        assert argc == 2
        if not sys.argv[1].isspace():
            assert sys.argv[1].replace(" ", "").isalnum()
    except AssertionError:
        print("AssertionError:"
              "Usage: [string containing alphanumeric characters or spaces]")
        return 1

    morse_code_list: list = [
        NESTED_MORSE[char.upper()]
        for char in sys.argv[1]
        if char.upper() in NESTED_MORSE
    ]
    morse_code: str = "".join(morse_code_list)
    print(morse_code)


if __name__ == "__main__":
    main()
