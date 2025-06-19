from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the specified file path and
    returns it as a NumPy array.

    Returns an image represented as a NumPy array.
    If the image cannot be loaded, returns None.
    """

    try:
        image: Image.Image = Image.open(path)
    except FileNotFoundError:
        print(f"Error: The file {path} does not exist.")
        return None
    except IOError:
        print(f"Error: Unable to read or decode the image from {path}.")
        return None
    except MemoryError:
        print("Error: Not enough memory to load the image.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    image_data: np.ndarray = np.array(image)
    print(f"The shape of the image is: {image_data.shape}")
    print(image_data)
    return image_data
