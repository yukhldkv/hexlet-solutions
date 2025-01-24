def build_query_string(params: dict) -> str:
    sorted_params = {key: params[key] for key in sorted(params)}
    result = ''
    for element in sorted_params:
        result += ('='.join([str(element), str(sorted_params[element])]))
        result += '&'
    result = result[:-1:]
    return result


def build_query_string_(params: dict) -> str:
    # Use a generator expression with sorted items
    return '&'.join(f"{key}={value}" for key, value in sorted(params.items()))


def main():
    print(build_query_string({'per': 10, 'page': 1}))
    print(build_query_string_({'per': 10, 'page': 1}))


if __name__ == "__main__":
    main()


# Query String (строка запроса) — это часть URL, содержащая константы и их значения. Она начинается после вопросительного знака и идет до конца адреса:

# # query string: page=5
# https://ru.hexlet.io/blog?page=5
# Если параметров несколько, то они отделяются амперсандом &:

# # query string: page=5&per=10
# https://ru.hexlet.io/blog?per=10&page=5
# src/solution.py
# Напишите функцию build_query_string, которая принимает на вход словарь с параметрами и возвращает строку запроса, сформированную из этих параметров:

# build_query_string({'per': 10, 'page': 1}) # 'page=1&per=10'
# Подсказки
# Тесты ожидают, что параметры будут отсортированы, поэтому воспользуйтесь функцией sorted().

# Чтобы собрать строку из нескольких кусков с помощью некоторого разделителя, вы можете воспользоваться таким способом:

# ','.join(['abc', 'cde', 'def']) # 'abc,cde,def'