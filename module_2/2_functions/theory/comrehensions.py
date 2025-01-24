def main():
    users = [
        { 'name': 'Igor', 'age': 19 },
        { 'name': 'Danil', 'age': 1 },
        { 'name': 'Vovan', 'age': 4 },
        { 'name': 'Matvey', 'age': 16 },
    ]

    filtered_users = list(filter(lambda user: user['age'] > 10, users))
    names = list(map(lambda user: user['name'], filtered_users))
    print(filtered_users)
    print(names)


if __name__ == "__main__":
    main()