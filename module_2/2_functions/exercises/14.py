from functools import reduce


def group_by_mark(acc, student, spec):
    acc.setdefault(student.get(spec), []).append(student)
    return acc


def group_by(student_list: list, spec: str) -> dict:
    result = reduce(lambda acc, student: group_by_mark(acc, student, spec), student_list, {})
    return result


# non-reduce version
def group_by_(list_of_dictionaries: list, group_spec: str) -> dict:
    result = {}
    for dictionary in list_of_dictionaries:
        mark = dictionary[group_spec]
        if mark not in result:
            result[mark] = []
        result[mark].append(dictionary)
    return result


def main():
    students = [
        {'name': 'Tirion', 'class': 'B', 'mark': 3},
        {'name': 'Keit', 'class': 'A', 'mark': 3},
        {'name': 'Ramsey', 'class': 'A', 'mark': 4},
    ]
    print(group_by_(students, 'mark'))
    print(group_by(students, 'mark'))


if __name__ == "__main__":
    main()


# Реализуйте функцию group_by для группировки объектов по заданному свойству. Функция принимает аргументами список словарей и название свойства для группировки. Она должна возвращать словарь, где ключ - это значение по заданному свойству, а значение - список с данными, подходящими для группы.

# Пример использования:

# from group_by import group_by

# students = [
#     {'name': 'Tirion', 'class': 'B', 'mark': 3},
#     {'name': 'Keit', 'class': 'A', 'mark': 3},
#     {'name': 'Ramsey', 'class': 'A', 'mark': 4},
# ]

# print(group_by([], ''))  # => {}
# print(group_by(students, 'mark'))

# # => {
# # =>   3: [
# # =>     {'name': 'Tirion', 'class': 'B', 'mark': 3},
# # =>     {'name': 'Keit', 'class': 'A', 'mark': 3},
# # =>   ],
# # =>   4: [
# # =>     {'name': 'Ramsey', 'class': 'A', 'mark': 4},
# # =>   ],
# # => }
# Подсказки
# Аналогичная функция есть в модуле itertools, но вам нужно создать её самостоятельно
# Алгоритм решения задачи с помощью цикла и функции reduce() одинаковый. Если вам так проще, сделайте сначала через цикл, затем перепишите через reduce()
# Решение этой задачи аналогично решению задачи users_by_age из теории