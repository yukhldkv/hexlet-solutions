def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    # print(factorial(997))
    
    return


if __name__ == "__main__":
    main()


# factorial(3)
# 3 * factorial(2)
# 3 * 2 * factorial(1)
# 3 * 2 * 1 * factorial(0)
# 3 * 2 * 1 * 1
# 3 * 2 * 1
# 3 * 2
# 6