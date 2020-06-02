"""This program demonstrates the work of timer decorator that records time even when an error occurs."""
import functools
import time


def timer(func):
    """Print the runtime of the decorated function."""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()

        try:
            value = func(*args, **kwargs)
            return value

        except ValueError as value_error:
            print(type(value_error), ' : ', value_error)
            raise ValueError('trouble after opening the file')

        except FileNotFoundError as no_file_error:
            print('Caught this error: ' + repr(no_file_error))
            raise FileNotFoundError('have some trouble')

        finally:
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

    return wrapper_timer


@timer
def get_data_from_file():
    """Get data after opening the file."""
    with open("test.txt", 'r') as file:
        data = file.read()
        num = int(data.strip())
        return data


get_data_from_file()
