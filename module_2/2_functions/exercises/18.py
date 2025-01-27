def length_nonrecursive(mylist: list) -> int:
    if len(mylist) == 0:
        return 0
    count = 1
    tail = mylist[1::]
    while tail:
        mylist = tail
        tail = mylist[1::]
        count += 1
    return count


def length(mylist: list) -> int:
    if not mylist:
        return 0
    return 1 + length(mylist[1:])


def reverse_range_nonrecursive(begin: int, end: int) -> list:
    result = []
    for x in range(end, begin - 1, -1):
        result.append(x)
    return result


def reverse_range(begin: int, end: int) -> list:
    if end < begin:
        return []
    return [end] + reverse_range(begin, end - 1)


def filter_positive(mylist: list):
    if not mylist:
        return []
    if mylist[0] > 0:
        return [mylist[0]] + filter_positive(mylist[1:])
    else:
        return filter_positive(mylist[1:])


def main():
    l = [1, 2, 3, 4, 5, 6]
    print(length(l))
    print(reverse_range(1, 10))
    print(filter_positive([1, -2, 3, -4]))
    return


if __name__ == "__main__":
    main()


# Привычные нам структуры можно представить и как рекурсивные. Например, у списка, есть голова (первый элемент) и хвост (последующие), у хвоста тоже есть своя голова и хвост, который тоже можно разделить на голову и хвост. И так далее до конца, где последний элемент списка можно представить как голова плюс хвост из пустого списка. А вот уже пустой список невозможно разделить, и наша рекурсия остановится.

# [1, 2, 3] # голова [1], хвост [2, 3]
# [2, 3] # голова [2], хвост [3]
# [3] # голова [3], хвост пустой список []
# [] # остановка
# В этом упражнении вам нужно будет реализовать три несложные функции, но через рекурсивный процесс:

# length() принимает список и возвращает его длину
# length([1, 2, 3]) # 3
# reverse_range() принимает два числа begin и end и возвращает перевернутый список всех чисел между. Для простоты договоримся, что begin <= end
# reverse_range(1, 1) # [1]
# reverse_range(1, 3) # [3, 2, 1]
# filter_positive() принимает список чисел и возвращает новый только с положительными элементами
# filter_positive([]) # []
# filter_positive([-3]) # []
# filter_positive([1, -2, 3]) # [1, 3]
# Вы, конечно, можете реализовать функции привычным итеративным способом, но попробуйте сменить угол зрения.