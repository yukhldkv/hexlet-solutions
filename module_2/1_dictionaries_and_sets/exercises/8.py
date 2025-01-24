# BEGIN (write your solution here)
def apply_diff(in_set: set, in_dict: dict):
    if "add" in in_dict:
        in_set.update(in_dict['add'])
    if "remove" in in_dict:
        in_set.difference_update(in_dict['remove'])
# END

target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
print(target)


# EXAMPLE
# BEGIN
def apply_diff(set_for_update, diff):
    set_for_update.update(diff.get('add', {}))
    set_for_update.difference_update(diff.get('remove', {}))
# END


# Так вот, для множеств существует несколько таких update-методов:

# difference_update
# intersection_update
# symmetric_difference_update
# update


# a.union(b)                 # аналог "a | b"
# a.intersection(b)          # аналог "a & b"
# a.difference(b)            # аналог "a - b"
# a.symmetric_difference(b)  # аналог "a ^ b"


# Цель упражнения — написать функцию apply_diff().

# Эта функция принимает два аргумента:

# Множество, которое нужно будет изменять по месту (возвращать ничего не нужно)
# Словарь, который может содержать ключи 'add' и 'remove' с множествами в качестве значений
# Значения по ключу 'add' нужно добавить в изменяемое множество, а значения по ключу 'remove' — убрать из множества. Прочие ключи в переданном словаре значения не имеют и обрабатываться не должны.

# target = {'a', 'b'}
# diff = {'add': {'c'}, 'remove': {'a'}}
# apply_diff(target, diff)
# print(target)  # => {'c', 'b'}
# Подсказки
# В этом упражнении нужно манипулировать множествами целиком, поэтому не нужно использовать методы add и discard