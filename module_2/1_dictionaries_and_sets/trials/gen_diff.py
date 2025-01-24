def gen_diff(first: dict, second: dict) -> dict:
    comparison = {}
    for element in first:
        if element in second:
            if first[element] == second[element]:
                comparison.setdefault(element, "unchanged")
            if first[element] != second[element]:
                comparison.setdefault(element, "changed")
        else:
            comparison.setdefault(element, "deleted")
    for element in second:
        if element not in first:
            comparison.setdefault(element, "added")
    return comparison


def gen_diff_(first: dict, second: dict) -> dict:
    comparison = {}
    all_keys = set(first) | set(second) # union
    for key in all_keys:
        if key in first and key in second:
            if first[key] == second[key]:
                comparison[key] = "unchanged"
            if first[key] != second[key]:
                comparison[key] = "changed"
        if key in first:
            comparison[key] = "deleted"
        else:
            comparison[key] = "added"
    return comparison


#EXAMPLE
# BEGIN
def gen_diff__(data1, data2):
    keys = data1.keys() | data2.keys()  # https://youtu.be/vkUTX1hruF8?t=929
    result = {}
    for key in keys:
        if key not in data1:
            result[key] = 'added'
        elif key not in data2:
            result[key] = 'deleted'
        elif data1[key] == data2[key]:
            result[key] = 'unchanged'
        else:
            result[key] = 'changed'
    return result
# END


def main():
    print(gen_diff_({"one": "eon", "two": "two", "four": True}, {"two": "own", "zero": 4, "four": True},))      


if __name__ == "__main__":
    main()


# Иногда в программировании возникает задача поиска разницы между двумя наборами данных — например, между словарями или json-файлами. Для этого даже существуют специальные сервисы, например, http://www.jsondiff.com/. Попробуйте нажать на ссылку sample data и затем кнопку Compare.

# src/solution.py
# Реализуйте функцию gen_diff, которая сравнивает два словаря и возвращает результат сравнения в виде словаря. Ключами результирующего словаря будут все ключи из двух входящих, а значением строка с описанием отличий: added, deleted, changed или unchanged.

# Возможные значения:

# added — ключ отсутствовал в первом словаре, но был добавлен во второй
# deleted — ключ был в первом словаре, но отсутствует во втором
# changed — ключ присутствовал и в первом и во втором словаре, но значения отличаются
# unchanged — ключ присутствовал и в первом и во втором словаре с одинаковыми значениями
# Пример работы:

# from solution import gen_diff

# gen_diff(
#     {"one": "eon", "two": "two", "four": True},
#     {"two": "own", "zero": 4, "four": True},
# )
# # {"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}