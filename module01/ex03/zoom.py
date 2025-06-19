from PIL import Image
from load_image import ft_load
import numpy as np


def ft_zoom() -> None:
    """
    Zooms into the center of the image using
    array slicing by the specified factor.
    """

    image_np: np.ndarray = ft_load("../images/animal.jpeg")
    if image_np is None:
        return
    height, width = image_np.shape[:2]
    factor: float = 1.5

    crop_width = int(width / factor)
    crop_height = int(height / factor)
    left: int = (width - crop_width) // 2
    top: int = (height - crop_height) // 2
    right: int = left + crop_width
    bottom: int = top + crop_height

    cropped_image_np: np.ndarray = image_np[top:bottom, left:right]
    cropped_image: Image.Image = Image.fromarray(cropped_image_np)
    zoomed_image: Image.Image = (
        cropped_image.resize((width, height), Image.LANCZOS)
    )

    print(f"New shape after slicing: {cropped_image_np.shape}")
    print(cropped_image_np)
    zoomed_image.save("./zoomed_animal.jpeg")
    # zoomed_image.show()


if __name__ == "__main__":
    ft_zoom()
