from load_image import ft_load
from PIL import Image
from os import path
import numpy as np
import sys


def ft_rotate(image_path: str) -> None:
    """
    Transposes the image to the left
    """

    image_np: np.ndarray | None = ft_load(image_path)
    if image_np is None:
        return
    height, width = image_np.shape[:2]

    transposed_image_np = np.zeros(
        (width, height, *image_np.shape[2:]), dtype=image_np.dtype
    )

    for i in range(height):
        for j in range(width):
            transposed_image_np[j, i] = image_np[i, j]
    print(f"New shape after transposing: {transposed_image_np.shape}")
    print(transposed_image_np)
    transposed_image: Image.Image = Image.fromarray(transposed_image_np)
    transposed_image.save(f"./transposed_{path.basename(image_path)}")
    # transposed_image.show()


def main():
    argc: int = len(sys.argv)
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
    ft_rotate(image_path)


if __name__ == "__main__":
    main()
