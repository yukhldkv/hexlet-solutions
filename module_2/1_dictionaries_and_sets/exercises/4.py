# BEGIN (write your solution here)
def collect_indexes(in_collection):
    result = {}
    for i in range (0, len(in_collection)):
        result.setdefault(in_collection[i], []).append(i)
    return result
# END


###
# Цель упражнения — написать функцию collect_indexes(). Эта функция должна:
# Принимать на вход коллекцию — некий итератор или итерируемый элемент
# Возвращать словарь или подобную ему коллекцию. Ключом будет элемент коллекции, а значением для ключа — список индексов коллекции, по которым встречается этот элемент
# d = collect_indexes("hello")
# d["h"]  # [0]
# d["e"]  # [1]
# d["l"]  # [2, 3]
###