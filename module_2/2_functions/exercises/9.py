# BEGIN (write your solution here)
def get_first_name(name_surname:str) -> str:
    result = ''
    for letter in name_surname:
        if letter == '_':
            return result
        result += letter

def sort_by(inner, names: list) -> list:
    return sorted(names, key = inner)
# END


def main():
    users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]
    print(sort_by(get_first_name, users))  # ["Boba_Fett", "Luke_Skywalker", "Vader_Darth"]
    # print(users) # => ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"] 

    users2 = ["Obi-Wan_Kenobi", "Jabba_Hutt", "Princess_Leia"]
    print(sort_by(get_first_name, users2))
    # print(users2)


if __name__ == "__main__":
    main()


# Вам предстоит реализовать пару функций:

# Функцию-ключ get_first_name(), которая получает имя пользователя из строки вида "Имя_Фамилия"
# get_first_name("Vader_Darth")  # Vader
# Функцию сортировки sort_by(), которая принимает функцию-ключ и список и сортирует список по этому ключу. Функция не должна изменять оригинальный список.
# users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

# sort_by(get_first_name, users)  # ["Boba_Fett", "Luke_Skywalker", "Vader_Darth"]
# print(users) # => ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"] 
# Подсказки
# Для сортировки используйте встроенную функцию sorted()