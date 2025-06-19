from load_image import ft_load
import sys


def main():
    argc: int = sys.argv.count()
    image_path: str = ""

    try:
        assert argc <= 2, "Usage: [image path]"
    except AssertionError as msg:
        print(msg)
        return

    if argc < 2:
        image_path = "../images/animal.jpeg"
    else:
        image_path = sys.argv[1]
    print(ft_load(image_path))


if __name__ == "__main__":
    main()
