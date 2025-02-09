# from functions import get_function


import os


def _right(collection, key, default=None):
    if key in collection:
        return collection[key]
    return default


def _fail1(collection, key, default=None):
    if key in collection:
        return collection[key]
    return None


def _fail2(collection, key, default=None):
    return default if default else collection[key]


def _fail3(collection, key, default=None):
    if (key in collection and default is None):
        return None
    return _right(collection, key, default)


functions = {
    "right": _right,
    "fail1": _fail1,
    "fail2": _fail2,
    "fail3": _fail3,
}


def get_function():
    name = os.environ['FUNCTION_VERSION']
    return functions[name]



get = get_function()

# BEGIN (write your solution here)
if get({"mykey": "myvalue"}, "mykey") != "myvalue":
    raise Exception('Функция работает неверно!')
if get({"mykey": "myvalue"}, "mykey1", "defaultvalue") != "defaultvalue":
    raise Exception('Функция работает неверно!')
if get({"mykey": "myvalue"}, "mykey", "defaultvalue") != "myvalue":
    raise Exception('Функция работает неверно!')
# END



# Напишите тесты для функции get(collection, key, default_value). Эта функция извлекает значение из словаря при условии, что ключ существует. В ином случае возвращается default_value:

# from functions import get_function
# get = get_function()

# get({"hello": "world"}, "hello")  # world
# get({"hello": "world"}, "hello", "kitty")  # world
# get({}, "hello", "kitty")  # kitty
# Тесты должны быть построены по такому же принципу, как это описывалось в теории урока: проверка через if и исключение в случае провала теста.

# Для хорошего тестирования этой функции понадобится как минимум три теста. Нужно проверить:

# Возвращает ли функция нужное значение по существующему ключу (прямой тест на работоспособность)
# Возвращается ли значение по умолчанию, если ключа нет
# Возвращается ли значение по существующему ключу, даже если передано значение по умолчанию (тест пограничного случая)