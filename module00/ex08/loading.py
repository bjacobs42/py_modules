import sys
import time
import shutil


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """

    start_time = time.time()
    terminal_width = shutil.get_terminal_size().columns
    max_length: int = max(terminal_width - 43, 43)
    total: int = len(lst)
    progress: int = 0
    progress_char = '='

    def render_progress() -> None:
        """Calculates percentage, items per seconds, elapsed/remaing time,"""
        """then prints the loading bar with its status on stdout."""

        elapsed_time: float = time.time() - start_time
        avg_time_per_item: float = (
            elapsed_time / progress if progress > 0 else 0
        )
        remaining_time: float = avg_time_per_item * (total - progress)
        items_per_sec: float = (
            progress / elapsed_time if elapsed_time > 0 else 0
        )

        percent_unit: float = progress / total
        filled_length: int = round(percent_unit * (max_length - 1))
        percent: int = round(percent_unit * 100)

        elapsed: str = time.strftime("%M:%S", time.gmtime(elapsed_time))
        remaining: str = time.strftime("%M:%S", time.gmtime(remaining_time))

        progress_bar: str = progress_char * filled_length + '>'
        status: str = f"{elapsed}<{remaining}, {items_per_sec:.2f}it/s"

        sys.stdout.write(f"\r{percent:3}% | [{progress_bar:{max_length}}] | "
                         f"{progress}/{total} [{status}]")
        sys.stdout.flush()

    for item in lst:
        render_progress()
        yield item
        progress += 1
    render_progress()
