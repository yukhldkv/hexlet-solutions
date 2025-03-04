from hexlet.fs import mkdir, mkfile, get_children, get_name, is_file, get_meta, is_directory, flatten
import os


def find_files_by_name(node, string, path=''):
    name = get_name(node)
    current_path = f"{path}/{name}".rstrip('/')
    paths = []
    if is_file(node) and string in name:
        paths.append(current_path)
    children = get_children(node)
    for child in children:
        # list_names = list(map(lambda child: find_files_by_name(child, string, current_path), children))
        paths.extend(find_files_by_name(child, string, current_path))
    return paths

# teachers's solution
# BEGIN
def _find_files_by_name(tree, substr):
    def walk(node, ancestry):
        name = get_name(node)
        new_ancestry = os.path.join(ancestry, name)
        if is_file(node):
            return [] if name.find(substr) < 0 else new_ancestry
        children = get_children(node)
        paths = map(lambda child: walk(child, new_ancestry), children)
        return flatten(paths)
    return walk(tree, '')
# END


def main():
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('nginx.conf', {'size': 800}),
            ]),
            mkdir('consul', [
                mkfile('config.json'),
                mkfile('data'),
                mkfile('raft'),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000})
    ])
    print(find_files_by_name(tree, 'co')) # ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
    return


if __name__ == "__main__":
    main()


# Реализуйте функцию find_files_by_name(). Она должна принимать на вход файловое дерево и подстроку, а затем возвращать список файлов, имена которых содержат эту подстроку. Функция должна вернуть полные пути файлам:

# from hexlet.fs import mkdir, mkfile
# from solution import find_files_by_name
# tree = mkdir('/', [
#     mkdir('etc', [
#         mkdir('apache'),
#         mkdir('nginx', [
#             mkfile('nginx.conf', {'size': 800}),
#         ]),
#         mkdir('consul', [
#             mkfile('config.json'),
#             mkfile('data'),
#             mkfile('raft'),
#         ]),
#     ]),
#     mkfile('hosts', {'size': 3500}),
#     mkfile('resolve', {'size': 1000}),
# ])
# find_files_by_name(tree, 'co')
# # ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
# Подсказки
# Для реализации этой логики вам понадобится аккумулятор, в котором будет храниться путь от корня до текущего узла. При проваливании внутрь директорий к нему добавляется имя текущей директории. В остальном логика работы идентична примеру из теории
# Переменную с путем от корня до текущего узла можно назвать ancestry
# Для построения путей используйте функцию os.path.join()