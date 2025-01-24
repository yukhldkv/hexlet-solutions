# BEGIN (write your solution here)
def diff_keys(old: dict, new: dict) -> dict:
    oldset = set()
    newset = set()
    for element in old:
        oldset.add(element)
    for element in new:
        newset.add(element)
    result = {"kept": set(), "added": set(), "removed": set()}
    result["kept"] = oldset & newset
    result["added"] = newset - oldset
    result["removed"] = oldset - newset
    return result
# END


# EXAMPLE SOLUTION
# BEGIN
def diff_keys(old, new):
    old_keys = set(old)
    new_keys = set(new)
    return {
        'kept': old_keys & new_keys,
        'added': new_keys - old_keys,
        'removed': old_keys - new_keys,
    }
# END


# В этом упражнении вам предстоит анализировать изменения в старой и новой версии словаря. Вам нужно реализовать функцию diff_keys(), которая должна:

# Принимать два словаря-аргумента — старый и новый
# Возвращать словарь с результатами анализа
# Результирующий словарь должен содержать строго три ниже перечисленных ключа:

# 'kept' — множество ключей, которые присутствовали в старом словаре и остались в новом
# 'added' — множество ключей, которые отсутствовали в старом словаре, но появились в новом
# 'removed' — множество ключей, которые присутствовали в старом словаре, но в новый не вошли
# Обратите внимание, что в этом упражнении сравниваются только ключи, а не значения.

# diff_keys({'name': 'Bob', 'age': 42}, {})
# # {'kept': set(), 'added': set(), 'removed': {'name', 'age'}}
# diff_keys({}, {'name': 'Bob', 'age': 42})
# # {'kept': set(), 'added': {'name', 'age'}, 'removed': set()}
# diff_keys({'a': 2}, {'a': 1})
# # {'kept': {'a'}, 'added': set(), 'removed': set()}