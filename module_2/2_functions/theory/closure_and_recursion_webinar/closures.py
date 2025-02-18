# clear terminal messages on running the file
import os
os.system('clear')


def create_counter(number: int):
    x = number
    def counter():
        nonlocal x
        x += 1
        return x
    return counter

counter_from_10 = create_counter(10)
print(counter_from_10())
print(counter_from_10())
print(counter_from_10())
print(counter_from_10())
print(counter_from_10())

counter_from_5 = create_counter(5)
print(counter_from_5())
print(counter_from_5())
print(counter_from_5())
print(counter_from_5())
print(counter_from_5())


def make_power(exp: int):
    def power_of(number: int) -> int:
        return number ** exp
    return power_of


cube = make_power(3)
print(cube(10))
print(make_power(3)(10))


from functools import partial


def example(a, b, c, d):
    def closure(e):
        print(a, b, c, d, e)
    return closure

a = example(1, 2, 3, 4)
a(5)
a(6)
a(7)


import datetime


def logger(name):
    def log_message(message):
        print(f'{name} - {datetime.datetime.now()} - {message}')
    return log_message


error_log = logger("Error")
info_log = logger("Info")
error_log('FATAL Error - ZeroDivisionError')
info_log('user with id=456 is logged in')