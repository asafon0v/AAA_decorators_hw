import sys
from typing import Callable


# Task 3
def redirect_output(filepath: str) -> Callable:
    def wrapper_1(func: Callable) -> Callable:
        def wrapper_2():
            with open(filepath, 'w') as file:
                original_stdout = sys.stdout
                sys.stdout = file
                func()
                sys.stdout = original_stdout

        return wrapper_2

    return wrapper_1


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    calculate()
    with open('./function_output.txt', 'r') as ffile:
        print(ffile.read())
