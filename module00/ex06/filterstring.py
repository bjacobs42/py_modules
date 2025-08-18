from ft_filter import ft_filter
import sys


def main():
    argc: int = len(sys.argv)
    min_size: int

    try:
        assert argc == 3
        assert sys.argv[1].strip()
        min_size = int(sys.argv[2])
    except AssertionError:
        print("AssertionError: Usage: [string, integer]")
        return 1

    min_size = int(sys.argv[2])
    words: list = sys.argv[1].split()
    filtered_words = ft_filter(lambda item: len(item) > min_size, words)
    print(filtered_words)


if __name__ == "__main__":
    main()
