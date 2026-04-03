from PIL import Image
from load_image import ft_load
from os import path
import numpy as np
import sys


def ft_zoom(image_path: str) -> None:
    """
    Zooms into the center of the image using
    array slicing by the specified factor.
    """

    image_np: np.ndarray | None = ft_load(image_path)
    if image_np is None:
        return
    height, width = image_np.shape[:2]
    factor: float = 1.5

    crop_width = max(1, int(width / factor))
    crop_height = max(1, int(height / factor))
    left: int = (width - crop_width) // 2
    top: int = (height - crop_height) // 2
    right: int = left + crop_width
    bottom: int = top + crop_height

    cropped_image_np: np.ndarray = image_np[top:bottom, left:right]
    cropped_image: Image.Image = Image.fromarray(cropped_image_np)
    zoomed_image: Image.Image = cropped_image.resize(
        (width, height), resample=Image.Resampling.LANCZOS
    )

    print(f"New shape after slicing: {cropped_image_np.shape}")
    print(cropped_image_np)
    zoomed_image.save(f"zoomed_{path.basename(image_path)}")
    # zoomed_image.show()


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
    ft_zoom(image_path)


if __name__ == "__main__":
    main()
