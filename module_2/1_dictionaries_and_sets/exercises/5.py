# BEGIN (write your solution here)
def all_unique(in_collection) -> bool:
    return len(set(in_collection)) == len(in_collection)
# END

all_unique([1, 2, 3, 3])


# Вам предстоит реализовать функцию all_unique(). Эта функция должна принимать коллекцию и возвращать True, если элементы не повторяются (если элементов нет, то ничего не повторяется).
# Посмотрим на пример работы этой функции:

# all_unique([])
# True
# all_unique([1, 2, 3])
# True
# all_unique([1, 2, 1])
# False