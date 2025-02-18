import copy
from hexlet.fs import mkdir, mkfile, get_children, get_name, get_meta, is_file, is_directory


# def downcase_file_names(node):
#     new_tree = {}
#     name = get_name(node).lower()
#     new_meta = copy.deepcopy(get_meta(node))
#     children = get_children(node)
#     new_children = list(map(lambda child: downcase_file_names(child), children))
#     new_tree = mkdir(name, new_children, new_meta)
#     return new_tree


def downcase_file_names(node):
    children = get_children(node)

    def downcase_names(node):
        if is_file(node):
            name = get_name(node).lower()
            new_meta = copy.deepcopy(get_meta(node))
            return mkfile(name, new_meta)
        elif is_directory(node):
            return downcase_file_names(node)

    new_children = list(map(downcase_names, children))
    new_meta = copy.deepcopy(get_meta(node))
    return mkdir(get_name(node), new_children, new_meta)



def main():
    tree = mkdir('/', [
        mkdir('eTc', [
            mkdir('NgiNx', [], {'size': 4000}),
            mkdir(
                'CONSUL',
                [mkfile('config.JSON', {'uid': 0})],
            ),
        ]),
        mkfile('HOSTS'),
    ])
    new_tree = downcase_file_names(tree)
    new_file = get_children(new_tree)[1]
    print(get_name(new_file))  # hosts
    print(new_tree)
    return


if __name__ == "__main__":
    main()

# Реализуйте функцию downcase_file_names(). Она должна принимать на вход директорию (объект-дерево) и приводить имена всех файлов к нижнему регистру, причем в корневой директории и во всех вложенных. Функция должна возвращать результат в виде обработанной директории:

# from hexlet.fs import mkdir, mkfile, get_children, get_name
# from solution import downcase_file_names
# tree = mkdir('/', [
#     mkdir('eTc', [
#         mkdir('NgiNx', [], {'size': 4000}),
#         mkdir(
#             'CONSUL',
#             [mkfile('config.JSON', {'uid': 0})],
#         ),
#     ]),
#     mkfile('HOSTS'),
# ])
# new_tree = downcase_file_names(tree)
# new_file = get_children(new_tree)[1]
# get_name(new_file)  # hosts
# Подсказки
# Придерживайтесь идеи иммутабельности - функция должна возвращать новое дерево, значит его метаданные должны быть скопированны (deep copy), а не ссылаться на оригинальные