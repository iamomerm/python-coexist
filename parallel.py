from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager


@contextmanager
def parallel(max_workers: int = None):
    """
    Execute nested code lines concurrently

    Example:

    with parallel() as pl:
        pl(lambda: print("Hello"))  # Thread 1
        pl(lambda: print("World"))  # Thread 2
    """
    tasks = []

    def submit(func: callable):
        if not callable(func):
            raise TypeError(
                '\nTypeError detected: This usually means "parallel" was used incorrectly ..\n\n'
                'Valid usage example:\n'
                'with parallel() as pl:\n'
                '    pl(lambda: print("Hello"))\n'
                '    pl(lambda: print("World"))'
            )
        tasks.append(func)

    yield submit

    with ThreadPoolExecutor(max_workers=max_workers or len(tasks)) as executor:
        futures = [executor.submit(task) for task in tasks]
        for future in futures:
            future.result()
