from loading import ft_tqdm
from tqdm import tqdm
import time


def main():
    items: int = 300
    print(tqdm.__doc__)
    for element in ft_tqdm(range(items)):
        time.sleep(.05)
    print()
    for element in tqdm(range(items)):
        time.sleep(.05)


if __name__ == "__main__":
    main()
