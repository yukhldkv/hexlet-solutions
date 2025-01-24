from itertools import chain


def get_girl_friends(users:list):
    friends = map(lambda friend: friend["friends"], users)
    female_friends = filter(lambda friend: friend["gender"] == 'female', chain.from_iterable(friends))
    return list(female_friends)


def main():
    users = [
        {
            'name': 'Tirion',
            'friends': [
                {'name': 'Mira', 'gender': 'female'},
                {'name': 'Ramsey', 'gender': 'male'},
            ],
        },
        {'name': 'Bronn', 'friends': []},
        {
            'name': 'Sam',
            'friends': [
                {'name': 'Aria', 'gender': 'female'},
                {'name': 'Keit', 'gender': 'female'},
            ],
        },
        {
            'name': 'Rob',
            'friends': [
                {'name': 'Taywin', 'gender': 'male'},
            ],
        },
    ]

    print(get_girl_friends(users))


if __name__ == "__main__":
    main()

# Реализуйте функцию get_girl_friends(), которая принимает на вход список пользователей и возвращает плоский список подруг всех пользователей (без сохранения ключей). Друзья каждого пользователя хранятся в виде списка в ключе 'friends'. Пол доступен по ключу 'gender' и может принимать значения 'male' или 'female'.

# Пример использования:

# from users import get_girl_friends

# users = [
#     {
#         'name': 'Tirion',
#         'friends': [
#             {'name': 'Mira', 'gender': 'female'},
#             {'name': 'Ramsey', 'gender': 'male'},
#         ],
#     },
#     {'name': 'Bronn', 'friends': []},
#     {
#         'name': 'Sam',
#         'friends': [
#             {'name': 'Aria', 'gender': 'female'},
#             {'name': 'Keit', 'gender': 'female'},
#         ],
#     },
#     {
#         'name': 'Rob',
#         'friends': [
#             {'name': 'Taywin', 'gender': 'male'},
#         ],
#     },
# ]

# print(get_girl_friends(users))
# # => [
# # =>     {'name': 'Mira', 'gender': 'female'},
# # =>     {'name': 'Aria', 'gender': 'female'},
# # =>     {'name': 'Keit', 'gender': 'female'},
# # => ]
# Другие примеры смотрите в модуле с тестами.

# Подсказки:
# Так как нам нужны только друзья, то можно применить функцию map() и получить список друзей, который затем будет фильтроваться
# Одно из решений задачи предполагает использование функции itertools.chain() для "выравнивания" списка списков