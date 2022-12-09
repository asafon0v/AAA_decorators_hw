import sys
from datetime import datetime as dt
from typing import Union

# Task 1
original_write = sys.stdout.write


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

if __name__ == '__main__':
    print('1, 2, 3')
    sys.stdout.write = original_write
    print('1, 2, 3')
