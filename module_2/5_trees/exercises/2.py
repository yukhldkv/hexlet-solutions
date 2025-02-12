import itertools


def remove_first_level(tree):
    result = []
    # for element in tree:
    #     if isinstance(element, list):
    #         result += element

    # result = [item for sublist in tree if isinstance(sublist, list) for item in sublist]
    
    return result


def main():
    tree1 = [[5], 1, [3, 4]]
    print(remove_first_level(tree1))  # [5, 3, 4]
    return


if __name__ == "__main__":
    main()


# В этом задании под деревом понимается любой список элементов, которые в свою очередь могут быть также деревьями или списками. Например:

# [
#   3, # Лист
#   [5, 3], # Узел
#   [[2]] # Узел
# ]
# Больше примеров вы можете найти в тестах.

# solution.py
# Реализуйте функцию remove_first_level(). Она должна принимать на вход дерево и возвращать новое дерево, элементами которого являются потомки вложенных узлов:

# from solution import remove_first_level

# tree1 = [[5], 1, [3, 4]]
# remove_first_level(tree1)  # [5, 3, 4]
# tree2 = [1, 2, [3, 5], [[4, 3], 2]]
# remove_first_level(tree2)  # [3, 5, [4, 3], 2]
# Подсказки
# Подключенный в модуле пакет itertools можно использовать, но это необязательно