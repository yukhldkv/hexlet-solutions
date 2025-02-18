from hexlet.fs import mkdir, mkfile, get_children, get_name, is_file, get_meta


# def get_dirs_and_files_list(node)->list:
#     result = []
#     children = get_children(node)
#     for child in children:
#         result.append(get_name(child))
#     return result


def calculate_size(node):
    if is_file(node):
        return get_meta(node)['size']
    children = get_children(node)
    return sum(map(calculate_size, children))


def du(node):
    result = []
    for child in get_children(node):
        result.append((get_name(child), calculate_size(child)))
    result.sort(key = lambda item: item[1], reverse = True)
    return result 


def test_du():
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('nginx.conf', {'size': 800}),
            ]),
            mkdir('consul', [
                mkfile('.config.json', {'size': 1200}),
                mkfile('data', {'size': 8200}),
                mkfile('raft', {'size': 80}),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])
    assert du(tree) == [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
    expected = [('consul', 9480), ('nginx', 800), ('apache', 0)]
    assert du(get_children(tree)[0]) == expected


def main():
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('nginx.conf', {'size': 800}),
            ]),
            mkdir('consul', [
                mkfile('.config.json', {'size': 1200}),
                mkfile('data', {'size': 8200}),
                mkfile('raft', {'size': 80}),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])
    print(du(tree))  # [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
    # test_du()
    print(du(get_children(tree)[0]))
    return


if __name__ == "__main__":
    main()
    
    
# В Linux, MacOS и многих операционных системах существует утилита du. Она умеет подсчитывать, сколько места занимают указанные файлы и директории. Например, так:

#  tmp$ du -sh *
#  97k	.venv
#   0B	com.docker.vmnetd.socket
#  10M	credo
# 4.0K	debug.mjs
#   0B	filesystemui.socket
# 4.0K	index.py
#  88K	poetry-lock.json
#  22M	taxdome
# Перед решением этого задания обязательно попрактикуйтесь с этой утилитой в терминале, посмотрите ее опции через man du. Экспериментировать нужно в локально установленной операционной системе.

# solution.py
# Реализуйте функцию du. Она должна принимать на вход директорию и возвращать:

# Список всех директорий и файлов, которые вложены в указанную директорию на один уровень
# Размер всей директории, который складывается из сумм всех размеров файлов, находящихся внутри во всех подпапках
# Так это выглядит в коде:

# from hexlet.fs import mkdir, mkfile
# from solution import du
# tree = mkdir('/', [
#     mkdir('etc', [
#         mkdir('apache'),
#         mkdir('nginx', [
#             mkfile('nginx.conf', {'size': 800}),
#         ]),
#         mkdir('consul', [
#             mkfile('.config.json', {'size': 1200}),
#             mkfile('data', {'size': 8200}),
#             mkfile('raft', {'size': 80}),
#         ]),
#     ]),
#     mkfile('hosts', {'size': 3500}),
#     mkfile('resolve', {'size': 1000}),
# ])
# du(tree)  # [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
# Примечания
# Размер файла задается в метаданных, при этом сами папки размера не имеют
# В структуре результирующего списка каждый элемент является кортежем с двумя значениями — именем директории и размером файлов внутри
# Результат отсортирован по размеру в обратном порядке — сверху тяжелые, снизу легкие
# Подсказки
# sort