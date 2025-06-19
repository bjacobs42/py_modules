from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_grey
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
        image_path = "../images/landscape.jpeg"
    else:
        image_path = sys.argv[1]

    array = ft_load(image_path)
    if array is not None:
        ft_invert(array)
        ft_red(array)
        ft_blue(array)
        ft_green(array)
        ft_grey(array)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
