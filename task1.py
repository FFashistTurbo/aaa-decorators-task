import sys
import datetime

original_write = sys.stdout.write


def my_write(string_text):
    now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    if string_text != '\n':
        return original_write('[' + now + ']: ' + string_text)
    return string_text


if __name__ == '__main__':

    sys.stdout.write = my_write

    print('1, 2, 3')
