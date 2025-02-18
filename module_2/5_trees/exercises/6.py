import copy
from hexlet.fs import mkdir, mkfile, get_children, get_name, get_meta, is_file, is_directory


def get_hidden_files_count(node):
    if is_file(node) and get_name(node).startswith("."):
        return 1
    children = get_children(node)
    hidden_files = list(map(get_hidden_files_count, children))
    return sum(hidden_files)


def main():
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('.nginx.conf', {'size': 800}),
            ]),
            mkdir('.consul', [
                mkfile('.config.json', {'size': 1200}),
                mkfile('data', {'size': 8200}),
                mkfile('raft', {'size': 80}),
            ]),
        ]),
        mkfile('.hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])
    print(get_hidden_files_count(tree))  # 3

    return


if __name__ == "__main__":
    main()


# Реализуйте функцию get_hidden_files_count(), которая считает количество скрытых файлов в директории и всех поддиректориях. В Linux-системах скрытыми считаются все файлы, название которых начинается с точки:

# from hexlet.fs import mkdir, mkfile
# from solution import get_hidden_files_count

# tree = mkdir('/', [
#     mkdir('etc', [
#         mkdir('apache'),
#         mkdir('nginx', [
#             mkfile('.nginx.conf', {'size': 800}),
#         ]),
#         mkdir('.consul', [
#             mkfile('.config.json', {'size': 1200}),
#             mkfile('data', {'size': 8200}),
#             mkfile('raft', {'size': 80}),
#         ]),
#     ]),
#     mkfile('.hosts', {'size': 3500}),
#     mkfile('resolve', {'size': 1000}),
# ])
# get_hidden_files_count(tree)  # 3