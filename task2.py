import sys
from task1 import my_write


def timed_output(function):
    original_write = sys.stdout.write

    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write
        output_value = function(*args, **kwargs)
        sys.stdout.write = original_write
        return output_value
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    result = print_greeting("Nikita")
    print(result)
