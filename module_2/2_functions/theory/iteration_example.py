def factorial(n):
    if n == 0:
        return 1
    
    def inner(counter, acc):
        if counter == 1:
            return acc
        return inner(counter - 1, counter * acc)
    
    return inner(n, 1) 


def main():
    print(factorial(5))


if __name__ == "__main__":
    main()