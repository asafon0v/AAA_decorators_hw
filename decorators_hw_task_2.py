import sys
from datetime import datetime as dt
from typing import Callable, Union


# Task 2
def timed_output(function: Callable) -> Callable:
    original_write = sys.stdout.write

    def wrapper(name: str) -> str:
        def my_write(string_text: str) -> Union[str, int]:
            """
            Дописывает к тексту текущие дату и время
            """
            string_text_with_time = f'{dt.now().strftime("[%Y-%m-%d %H:%M:%S]:")} {string_text}'

            if string_text == '\n':
                return original_write('\n')
            else:
                return original_write(string_text_with_time)

        sys.stdout.write = my_write
        function_res_with_time = function(name)
        sys.stdout.write = original_write

        return function_res_with_time

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting("Nikita")
