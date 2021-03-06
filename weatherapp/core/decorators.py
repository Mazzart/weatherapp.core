"""Decorators for the weather application."""

import time
import sys
from functools import lru_cache


def slow_down_one_second(func):
    """Waits one second before calling function."""

    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper


def slow_down(seconds=1):
    """Waits some time before calling function."""
    def one_second(func):
        """Waits one second before calling function."""

        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapper
    return one_second


@slow_down(seconds=3)
def hello(name):
    """Hello test function."""
    sys.stdout.write(f'Hello {name}\n')


def timer(func):
    """Finds function execution time."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # performance counter
        result = func(*args, **kwargs)
        run_time = time.perf_counter() - start_time
        sys.stdout.write(f'Function ({func.__name__!r}) execution time '
                         f'is {run_time:.4f} seconds.\n')
        return result

    return wrapper


@timer
def sleep(sec):
    """Sleep test function."""
    time.sleep(sec)


def get_arguments(func):
    """Prints all arguments passed to the function."""
    def wrapper(*args, **kwargs):
        for arg in args:
            sys.stdout.write(f'{arg}\n')
        for key, value in kwargs.items():
            sys.stdout.write(f'The value of {key} is {value}\n')
        return func(*args, **kwargs)

    return wrapper


@get_arguments
def print_arguments(first, second, third):
    """Print arguments test function."""
    sys.stdout.write(f'{first + second}\n')
    sys.stdout.write(f'{third}\n')


print_arguments(5, 6, third=97)


def func_calls_counter(func):
    """Counts how many times a function is called."""
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func(*args, **kwargs)

    wrapper.counter = 0
    return wrapper


@func_calls_counter
def print_anything():
    """Print_anything test function."""
    sys.stdout.write("Enter text to print here\n")


print_anything()
for item in range(3):
    print_anything()

sys.stdout.write(f'{print_anything.counter}\n')


# did not write my own decorator for caching
# just used the implementation from the standard library
@lru_cache(maxsize=256)
def fibonacci(num):
    """Return n-th Fibonacci number."""
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)


sys.stdout.write(f'The n-th Fibonacci number: {fibonacci(42)}\n')


def singleton(cls):
    """Singleton decorator"""
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
