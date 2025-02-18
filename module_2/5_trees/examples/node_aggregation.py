from hexlet import fs

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkfile('bashrc'),
        fs.mkfile('consul.cfg'),
    ]),
    fs.mkfile('hexletrc'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])

# В реализации используем рекурсивный процесс,
# чтобы добраться до самого дна дерева
def get_nodes_count(node):
    if fs.is_file(node):
        # Возвращаем 1 для учета текущего файла
        return 1
    # Если узел — директория, получаем его потомков
    children = fs.get_children(node)
    # Самая сложная часть
    # Считаем количество потомков для каждого потомка,
    # вызывая рекурсивно нашу функцию get_nodes_count
    descendant_counts = list(map(get_nodes_count, children))
    # Возвращаем 1 (текущая директория) + общее количество потомков
    return 1 + sum(descendant_counts)

get_nodes_count(tree)
# 8


from hexlet import fs

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkdir('apache'),
        fs.mkdir('nginx', [
            fs.mkfile('nginx.conf'),
        ]),
    ]),
    fs.mkdir('consul', [
        fs.mkfile('config.json'),
        fs.mkfile('file.tmp'),
        fs.mkdir('data'),
    ]),
    fs.mkfile('hosts'),
    fs.mkfile('resolve'),
])


def get_files_count(node):
    if fs.is_file(node):
        return 1
    children = fs.get_children(node)
    descendant_count = list(map(get_files_count, children))
    return sum(descendant_count)


def get_subdirectories_info(node):
    children = fs.get_children(node)
    # Нас интересуют только директории
    filtered = filter(fs.is_directory, children)
    # Запускаем подсчет для каждой директории
    return list(map(lambda child: (fs.get_name(child), get_files_count(child)), filtered))


print(get_subdirectories_info(tree))
# => [('etc', 1), ('consul', 2)]


items = [2, [3, [4, [5, [6]]], [7]]]

def aggregate(items):
    if isinstance(items, int):
        return items
    result = list(map(aggregate, items))
    return sum(result)

print(aggregate(items))


items = [2, [3, [4, [5, [6]]], [7]]]

def check(num):
    if num % 2 == 0 and num > 4:
        return num
    return 1

def aggregate(items):
    if isinstance(items, int):
        return check(items)
    result = list(map(aggregate, items))
    return sum(result)

aggregate(items) # 11


# Функция count_items() считает суммарное количество элементов в списке и во вложенных списках.

items = [2, ['a', [4, ['s', [6, [1.5]]]]]]

def count_items(items):
    if not isinstance(items, list):
        return 1
    result = sum(list(map(count_items, items)))
    return result

count_items(items) # 6