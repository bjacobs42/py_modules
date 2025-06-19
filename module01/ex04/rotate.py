from load_image import ft_load
from PIL import Image
import numpy as np


def ft_rotate() -> None:
    """
    Transposes the image
    """

    image_np: np.ndarray = ft_load("../images/animal.jpeg")
    if image_np is None:
        return
    height, width, channels = image_np.shape

    transposed_image_np = np.zeros(
            (width, height, channels), dtype=image_np.dtype)

    for i in range(height):
        for j in range(width):
            transposed_image_np[j, i, :] = image_np[i, j, :]

    print(f"New shape after Transpose: {transposed_image_np.shape}")
    print(transposed_image_np)
    transposed_image: Image.Image = Image.fromarray(transposed_image_np)
    transposed_image.save("./transposed_animal.jpeg")
    # transposed_image.show()


if __name__ == "__main__":
    ft_rotate()
