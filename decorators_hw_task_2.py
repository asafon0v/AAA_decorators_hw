import sys
from typing import Callable
from decorators_hw_task_1 import my_write, original_write


# Task 2

def timed_output(function: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write
        function_res = function(*args, **kwargs)
        sys.stdout.write = original_write

        return function_res

    return wrapper


@timed_output
def s(*args, **kwargs):
    return 22


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print(s(1, 2, 3, "aaa", True, name=11))
    print_greeting("Nikita")
