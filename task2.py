import sys
import datetime


def timed_output(function):
    original_write = sys.stdout.write

    def my_write(string_text):
        now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        if string_text != '\n':
            return original_write('[' + now + ']: ' + string_text)
        return string_text

    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write
        ret_val = function(*args, **kwargs)
        sys.stdout.write = original_write
        return ret_val
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting("Nikita")
