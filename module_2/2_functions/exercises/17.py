def partial_apply(func, word: str):
    def inner(*args):
        return func(word, args[0])
    return inner


def greet(name, surname):
    return f'Hello, {name} {surname}!'


def flip(func):
    def inner(*args):
        return func(args[1], args[0])
    return inner


def main():
    f = partial_apply(greet, 'Dorian')
    print(f('Grey'))
    f = flip(greet)
    print(f('Dorian', 'Grey'))

    return


if __name__ == "__main__":
    main()


# В этом упражнении вам нужно будет реализовать две функции высшего порядка, возвращающие замыкания: partial_apply() и flip().

# partial_apply() принимает функцию от двух аргументов и первый аргумент для неё, а возвращает замыкание. Замыкание принимает оставшийся второй аргумент, а затем применяет замкнутую функцию к обоим аргументам и возращает результат.

# def greet(name, surname):
#     return f'Hello, {name} {surname}!'

# f = partial_apply(greet, 'Dorian')
# f('Grey')
# # 'Hello, Dorian Grey!'
# Функция flip() принимает в качестве единственного аргумента функцию от двух аргументов. Возвращаемое замыкание должно также принять два аргумента, а затем применить к ним замкнутую функцию, но аргументы подставить в обратном порядке. Таким образом flip() как бы "переворачивает" ("flips") исходную функцию.

# def greet(name, surname):
#     return f'Hello, {name} {surname}!'

# f = flip(greet)
# f('Christian', 'Teodor')
# # 'Hello, Teodor Christian!'