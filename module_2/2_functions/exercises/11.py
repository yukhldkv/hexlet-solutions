def get_fibonacci():
    fib = [0, 1]
    prev = fib[-1]
    prevprev = fib[-2]
    fib_iter = iter(fib)
    while fib_iter:
        yield next(fib_iter)
        fib.append(prev + prevprev)
        prevprev = prev
        prev = fib[-1]



#EXAMPLE
# BEGIN
def get_fibonacci_example():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# END


def main():
    fib = get_fibonacci()
    for x in fib:
        print(x)
        if x > 10:
            break

if __name__ == "__main__":
    main()



# Одно из частых применений генераторов - это реализация бесконечных последовательностей. Реализуйте функцию get_fibonacci(), которая генерирует числа последовательности Фибоначчи. Напомним, что правило, по которой формируется последовательность можно записать так:

# # первые два числа
# a, b = 0, 1

# # последующие
# a, b = b, a + b
# Функция должна возвращать одно число, в примере выше это a

# Пример использования:

# fib = get_fibonacci()

# for x in fib:
#     print(x)
#     if x > 10:
#         break

# # => 0
# # => 1
# # => 1
# # => 2
# # => 3
# # => 5
# # => 8
# # => 13
# Подсказки
# Помните, что yield не заканчивает выполнение функции, и после него можно продолжить вычисления