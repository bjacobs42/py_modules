import sys


def main():
    argc: int = len(sys.argv)
    try:
        assert argc > 1, "no argument provided"
        assert argc == 2, "more than one argument provided"
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return 1

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return 1

    if number % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")


if __name__ == "__main__":
    main()
