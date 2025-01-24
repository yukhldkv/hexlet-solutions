from itertools import chain


def get_children(users: list):
    callback = lambda child: child['children']
    children = map(callback, users)
    return list(chain.from_iterable(children))

def main():
    users = [
    {
        'name': 'Tirion',
        'children': [
            {'name': 'Mira', 'birthday': '1983-03-23'},
        ],
    },
    {'name': 'Bronn', 'children': []},
    {
        'name': 'Sam',
        'children': [
            {'name': 'Aria', 'birthday': '2012-11-03'},
            {'name': 'Keit', 'birthday': '1933-05-14'},
        ],
    },
    {
        'name': 'Rob',
        'children': [
            {'name': 'Tisha', 'birthday': '2012-11-03'},
        ],
    },
    ]
    print(get_children(users))
    # print(list(chain(users)))


if __name__ == "__main__":
    main()

# Реализуйте функцию get_children(), которая принимает на вход список пользователей и возвращает плоский список их детей. Дети каждого пользователя хранятся в виде списка в ключе 'children'.

# Пример использования:

# from users import get_children

# users = [
#     {
#         'name': 'Tirion',
#         'children': [
#             {'name': 'Mira', 'birthday': '1983-03-23'},
#         ],
#     },
#     {'name': 'Bronn', 'children': []},
#     {
#         'name': 'Sam',
#         'children': [
#             {'name': 'Aria', 'birthday': '2012-11-03'},
#             {'name': 'Keit', 'birthday': '1933-05-14'},
#         ],
#     },
#     {
#         'name': 'Rob',
#         'children': [
#             {'name': 'Tisha', 'birthday': '2012-11-03'},
#         ],
#     },
# ]

# print(get_children(users))
# # => [
# # =>     {'name': 'Mira', 'birthday': '1983-03-23'},
# # =>     {'name': 'Aria', 'birthday': '2012-11-03'},
# # =>     {'name': 'Keit', 'birthday': '1933-05-14'},
# # =>     {'name': 'Tisha', 'birthday': '2012-11-03'},
# # => ]
# Другие примеры смотрите в модуле с тестами.

# Подсказки
# chain.from_iterable()