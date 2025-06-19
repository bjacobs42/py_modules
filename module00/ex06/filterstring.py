from ft_filter import ft_filter
import sys


def main():
    argc: int = len(sys.argv)
    try:
        assert argc == 3
        assert sys.argv[1].strip()
        assert sys.argv[2].isdigit()
    except AssertionError:
        print("AssertionError: Usage: [string, positive integer]")
        return 1

    min_size = int(sys.argv[2])
    words: list = sys.argv[1].split()
    filtered_words = ft_filter(lambda item: len(item) > min_size, words)
    print(filtered_words)


if __name__ == "__main__":
    main()
