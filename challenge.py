import time


def finish_date(func):
    # You have to code here!!
    def wrapper(*args, **kwargs):

        initial_time = time.time()
        func(*args, **kwargs)
        final_time = time.time()
        duration = final_time - initial_time
        local_time = time.localtime()
        finalization_time = time.strftime("%d/%m/%Y - %H:%M:%S", local_time)
        print('Function {} ended its execution at: {} . And it took {} seconds to be executed'.format(func.__name__, finalization_time, round(duration, 6)))

    return wrapper


@finish_date
def palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


@finish_date
def long_function():
    for _ in range(1000000):
        pass


def run():
    palindrome('Ana')
    long_function()


if __name__ == '__main__':
    run()
