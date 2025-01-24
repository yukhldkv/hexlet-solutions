def validate_passwords(password_list: list) -> bool:
    length_less_than_eight = any(len(password) < 8 for password in password_list)
    has_digits = [password for password in password_list if any(letter.isdigit() for letter in password)]
    at_least_one_upper_letter = [password for password in password_list if any(letter.isupper() for letter in password)]
    contains_spaces = [password for password in password_list if any(letter == ' ' for letter in password)]
    if length_less_than_eight or not has_digits or not at_least_one_upper_letter or contains_spaces:
        return False
    return True


# better version
def validate_passwords_v2(password_list: list) -> bool:
    for password in password_list:
        if (
            len(password) < 8 or
            not any(letter.isdigit() for letter in password) or
            not any(letter.isupper() for letter in password) or
            any(letter.isspace() for letter in password)
        ):
            return False
    return True


def main():
    passswords1 = ["password", "Example_", "v3ry_str0ng_passw0rd"]
    passswords2 = ["password", "word"]
    print(validate_passwords(passswords1))
    print(validate_passwords(passswords2))


if __name__ == "__main__":
    main()


# Создайте функцию validate_passwords(), которая принимает список паролей и проверяет их на соответствие следующим критериям:

# Все пароли должны быть не короче 8 символов.
# Хотя бы один пароль должен содержать цифру.
# Хотя бы один пароль должен содержать заглавную букву.
# Ни один пароль не должен содержать пробелов.
# Функция должна возвращать True, если все условия выполнены, и False в противном случае.

# Подсказки
# Используйте generator expressions в сочетании с функциями any и all для реализации этой проверки.