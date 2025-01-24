def format_person_info(name: str, age: int, **information) -> str:
    result = ""
    result += f"Name: {name}, Age: {age}, "
    sorted_keys = sorted(information.keys())
    for key in sorted_keys:
        result += f"{key.capitalize()}: {information[key]}, "
    if result[-1] == ' ' and result[-2] == ',':
        result = result[:-2:]
    return result


def main():
    basic_info = ('Alice', 30)
    additional_info = {'city': 'New York', 'job': 'Engineer', 'hobby': 'painting'}
    result = format_person_info(*basic_info, **additional_info)
    print(result)


if __name__ == "__main__":
    main()


# EXAMPLE
# BEGIN 
def format_person_info(name, age, **kwargs):
    base_info = f"Name: {name}, Age: {age}"

    if kwargs:
        additional_info = []
        for key, value in sorted(kwargs.items()):
            additional_info.append(f"{key.capitalize()}: {value}")
        return f"{base_info}, {", ".join(additional_info)}"
    else:
        return base_info
# END

# Реализуйте функцию format_person_info(), которая принимает имя и возраст как обязательные параметры, а также может принимать любое количество дополнительных именованных аргументов с другой информацией о человеке.

# Функция должна возвращать отформатированную строку с информацией о человеке.

# Пример использования:

# basic_info = ('Alice', 30)
# additional_info = {'city': 'New York', 'job': 'Engineer', 'hobby': 'painting'}

# result = format_person_info(*basic_info, **additional_info)
# print(result) # => Name: Alice, Age: 30, City: New York, Job: Engineer, Hobby: painting
# Подсказки
# Используйте f-строки для форматирования вывода
# Отсортируйте дополнительную информацию по ключам в алфавитном порядке