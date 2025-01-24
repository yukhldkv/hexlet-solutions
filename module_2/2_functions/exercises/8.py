def run(text):
    # BEGIN (write your solution here)
    take_last = lambda text, num: text[-1: -num - 1: -1] if len(text) >= num else None
    # END
    return take_last(text, 4)


def main():
    print(run('hexlet'))
    print(run(''))       # None
    print(run('cb'))     # None
    print(run('power'))  # rewo
    print(run('kids'))


if __name__ == "__main__":
    main()


# EXAMLE
# BEGIN
    def take_last(string, length):
        if not string or len(string) < length:
            return None

        return string[-length:][::-1]
    # END


# Реализуйте внутреннюю функцию take_last(), которая возвращает последние n символов строки в обратном порядке. Количество символов передаётся в take_last() вторым параметром. Если передаётся пустая строка или строка меньше необходимой длины, функция должна вернуть None.

# Примеры

# # функция run использует take_last внутри


# run('')       # None
# run('cb')     # None
# run('power')  # rewo
# run('hexlet') # telx