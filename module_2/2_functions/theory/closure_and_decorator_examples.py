from decimal import Decimal
import time


def sum(a):
    def inner(b):
        return a + b
    return inner


def special_sum():
    count = 1
    def inner(b):
        nonlocal count
        count += b
        return count
    return inner


def calc_time(func):
    def inner(*args, **kwargs):
        #start = time.time() # float
        start = Decimal(time.time())
        res = func(*args, **kwargs)
        finish = Decimal(time.time())
        print(finish - start)
        return res
    return inner


@calc_time
def large_logic(a, b):
    #time.sleep(1)
    return a + b


def main():
    # func2 = sum(1) # замыкание
    # print(func2(2))
    # res = sum(1)(2) # карирование
    # print(res)

    # Пример замыкания значения переменной внутри вызова функции
    # do_special = special_sum()
    # print(do_special(1))
    # print(do_special(1))
    # print(do_special(1))

    large_logic(1, 2)
    large_logic(1, 2)
    large_logic(1, 2)

    res = large_logic(1, 2)
    print(res)

    return 


if __name__ == "__main__":
    main()


# https://disk.yandex.ru/d/1NdpQQUqtdjing/2024-12-27_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80-%D0%A7%D0%B5%D0%BF%D0%B0%D0%B9%D0%BA%D0%B8%D0%BD_%D0%9B%D0%B0%D0%B9%D0%B2%D0%BA%D0%BE%D0%B4%D0%B8%D0%BD%D0%B3-%22%D0%94%D0%B5%D0%BA%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D1%8B-%D0%B8-%D0%B7%D0%B0%D0%BC%D1%8B%D0%BA%D0%B0%D0%BD%D0%B8%D1%8F%22-%D0%B4%D0%BB%D1%8F-%D1%81%D1%82%D1%83%D0%B4%D0%B5%D0%BD%D1%82%D0%BE%D0%B2-2-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8F
# 33:25