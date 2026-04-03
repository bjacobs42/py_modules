from PIL import Image
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received as a numpy array.

    Returns a numpy array of the image result.
    """

    inverted_np: np.ndarray = 255 - array
    inverted_image = Image.fromarray(inverted_np)
    inverted_image.save("./inverted_image.jpeg")
    # inverted_image.show()
    return inverted_np


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Sets green and blue channel to zero (red scaling)
    in the image received as a numpy array.

    Returns a numpy array of the image result.
    """

    red_np: np.ndarray = np.copy(array)
    if array.ndim > 2:
        red_np[:, :, 1:3] = 0

    red_image = Image.fromarray(red_np)
    red_image.save("./red_image.jpeg")
    # red_image.show()
    return red_np


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Sets blue and red channel to zero (green scaling)
    in the image received as a numpy array.

    Returns a numpy array of the image result.
    """

    green_np: np.ndarray = np.copy(array)
    if array.ndim > 2:
        green_np[:, :, [0, 2]] = 0

    green_image = Image.fromarray(green_np)
    green_image.save("./green_image.jpeg")
    # green_image.show()
    return green_np


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Sets green and red channel to zero (blue scaling)
    in the image received as a numpy array.

    Returns a numpy array of the image result.
    """

    blue_np: np.ndarray = np.copy(array)
    if array.ndim > 2:
        blue_np[:, :, 0:2] = 0

    blue_image = Image.fromarray(blue_np)
    blue_image.save("./blue_image.jpeg")
    # blue_image.show()
    return blue_np


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Divides each channel with grey scale formula values,
    grey scaling the image received as a numpy array.

    Returns a numpy array of the image result.
    """

    grey_np: np.ndarray = np.copy(array)
    if array.ndim > 2:
        grey_np = (
            grey_np[:, :, 0] / 3.3445
            + grey_np[:, :, 1] / 1.704
            + grey_np[:, :, 2] / 8.7719
        ).astype(np.uint8)

    grey_image = Image.fromarray(grey_np)
    grey_image.save("./grey_image.jpeg")
    # grey_image.show()
    return grey_np
