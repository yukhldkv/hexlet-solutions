def memoized(func):
    memory = {}
    def inner(x):
        if x not in memory:
            memory.setdefault(x, func(x))
        return memory.get(x)
    return inner

@memoized
def f(x):
    print('Calculating...')
    return x * 10


def main():
    print(f(1))
    print(f(42))
    print(f(2))
    print(f(2))
    print(f(42))

if __name__ == "__main__":
    main()


# EXAMPLE
# BEGIN
def memoized(function):
    memory = {}

    def inner(argument):
        memoized_result = memory.get(argument)
        if memoized_result is None:
            memoized_result = function(argument)
            memory[argument] = memoized_result
        return memoized_result

    return inner
# END


# Вам предстоит реализовать декоратор, добавляющий функции мемоизацию. Мемоизация — это запоминание уже вычисленных результатов для уже однажды встреченных аргументов.

# Для простоты будем считать, что мемоизироваться будут численные функции одного аргумента (аргумент — число, результат — то же число). Полученный результат должен возвращаться.

# f = memoized(f)
# from solution import memoized 
# @memoized
# def f(x):
#     print('Calculating...')
#     return x * 10

# f(1)
# # => Calculating...
# # 10
# f(1)
# # 10
# f(42)
# # => Calculating...
# # 420
# f(42)
# # 420
# f(1)
# # 10
# Заметьте, что для каждого нового аргумента выводится сообщение "Calculating...", но только лишь один раз.