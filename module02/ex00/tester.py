from load_csv import load
import sys


def main():
    try:
        assert len(sys.argv) == 2, "Usage: [csv file path]"
    except AssertionError as e:
        print(f"Assert error: {e}")
        return

    print(load(sys.argv[1]))


if __name__ == "__main__":
    main()
