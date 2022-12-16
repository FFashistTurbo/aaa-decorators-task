import sys


def redirect_output(filepath):
    def decorator(function):
        def wrapper():
            original_out = sys.stdout
            with open(filepath, 'w') as output:
                sys.stdout = output
                output_value = function()

            sys.stdout = original_out
            return output_value

        return wrapper
    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    calculate()
