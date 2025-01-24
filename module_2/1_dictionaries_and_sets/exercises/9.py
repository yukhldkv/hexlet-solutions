# from hash_table import get_hash


class HashTable(list):
    def __setitem__(self, index, value):
        try:
            super().__setitem__(index, value)
        except IndexError:
            for _ in range(index - len(self) + 1):
                self.append(None)
            super().__setitem__(index, value)

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return None

    def set(self, key, value):
        index = get_hash(key)
        self[index] = [key, value]


def make_table():
    return HashTable()


def get_hash(key):
    return sum(ord(ch) for ch in key) % 10 + 1


# BEGIN (write your solution here)
def get_or_default(hashtable, key, default):
    result = hashtable.__getitem__(get_hash(key))
    if result == None:
        return default
    return result[1]
# END

# EXAMPLE
# BEGIN
def get_or_default(map, key, default):
    index = get_hash(key)
    data = map[index]
    if data is None:
        return default
    _, value = data
    return value
# END

# Реализуйте функцию get_or_default(). Она должна возвращать из хеш-таблицы значение по ключу или значение по умолчанию, если такой записи не существует.

# hash_table = make_table()
# # метод set(ключ, значение) записывает значение по ключу в мапу
# hash_table.set("g", "bar")
# hash_table.set("e", "foo")

# get_or_default(hash_table, "g", "python") # bar
# get_or_default(hash_table, "a", "python") # python
# Хеш-таблица представляет собой список, содержащий пары (ключ, значение) по индексам. Индексы рассчитываются из результата применения хеш-функции get_hash() к ключу. Если записи по такому индексу еще нет, то вместо пары хранится None.

# # функция get_hash() превращает ключ в хеш-число, которое дальше будет индексом этого ключ
# get_hash('e') # 2
# get_hash('f') # 3
# get_hash('g') # 4

# # хеш-таблица внутри использует функцию get_hash() для расчета индексов
# hash_table = make_table()
# hash_table.set("e", "foo")
# hash_table.set("f", "baz")
# hash_table.set("g", "bar")

# # по расчитаным индексам хранятся ключи и значения
# print(hash_table) # => [None, None, ('e', 'foo'), ('f', 'baz'), ('g', 'bar')]
