def main():
    users = [
        { 'name': 'Igor', 'amount': 19 },
        { 'name': 'Danil', 'amount': 1 },
        { 'name': 'Ivan', 'amount': 4 },
        { 'name': 'Matvey', 'amount': 16 },
    ]

    sum = 0
    for user in users:
        sum += user['amount']

    print(sum) # => 40

    users = [
        { 'name': 'Petr', 'age': 4 },
        { 'name': 'Igor', 'age': 19 },
        { 'name': 'Ivan', 'age': 4 },
        { 'name': 'Matvey', 'age': 16 },
    ]
    
    users_by_age = {}
    for user in users:
        age = user['age']
        name = user['name']
        # Проверяем, добавлен ли уже ключ age в результирующий словарь или нет
        if age not in users_by_age:
            users_by_age[age] = []
        users_by_age[age].append(name)

    print(users_by_age)


if __name__ == "__main__":
    main()