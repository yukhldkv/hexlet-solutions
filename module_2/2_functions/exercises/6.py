# BEGIN (write your solution here)
def get_average(*args):
    if len(args) == 0:
        return None
    result = 0
    for element in args:
        result += element
    return result / len(args)
# END


# EXAMPLE
# BEGIN
def get_average(*numbers):
    count = len(numbers)
    if not count:
        return None
    return sum(numbers) / count
# END


# Реализуйте функцию get_average(), которая возвращает среднее арифметическое всех переданных аргументов. Если функции не передать ни одного аргумента, то она должна вернуть None.

# Примеры

# get_average(0) # 0
# get_average(0, 10) # 5
# get_average(-3, 4, 2, 10) # 3.25
# get_average() # None