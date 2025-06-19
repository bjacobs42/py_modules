from datetime import datetime


def print_seconds_since_epoch():
    now = datetime.now()
    seconds_since_epoch: float = now.timestamp()

    formatted_seconds: str = f"{seconds_since_epoch:,.4f}"
    scientific_seconds: str = f"{seconds_since_epoch:,e}"
    date: str = f"{now:%b %d, %Y}"

    print(f"Seconds since January 1, 1970: {formatted_seconds}",
          f"or {scientific_seconds} in scientific notation")
    print(date)


print_seconds_since_epoch()
