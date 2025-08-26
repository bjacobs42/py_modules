from load_image import ft_load
import sys


def main():
    argc: int = len(sys.argv)
    image_path: str = ""

    if argc > 2:
        print("Usage: [image path]")
        return
    if argc < 2:
        image_path = "../images/animal.jpeg"
    else:
        image_path = sys.argv[1]
    print(ft_load(image_path))


if __name__ == "__main__":
    main()
