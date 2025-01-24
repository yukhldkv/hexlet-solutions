# BEGIN (write your solution here)
def count_all(source) -> dict:
    result = {}
    for element in source:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result
# END


# EXAMPLE SOLUTION
# BEGIN
def count_all(items):
    counters = {}
    for item in items:
        counters[item] = counters.get(item, 0) + 1
    return counters
# END


# Цель упражнения — функция count_all(). Эта функция должна принимать на вход итерируемый источник и возвращать словарь. Ключами этого словаря должны стать элементы источника, при этом значения должны отражать количество повторов элемента в коллекции-источнике.

# Посмотрим на этих примерах, как должна работать эта функция:

# count_all(["cat", "dog", "cat"])  # {"cat": 2, "dog": 1}
# count_all("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# count_all("*" * 20)  # {'*': 20}