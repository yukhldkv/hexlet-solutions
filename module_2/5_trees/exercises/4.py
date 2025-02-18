import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile, is_directory


# BEGIN (write your solution here)
def traverse_tree(node):
    # if node["type"] == "file":
    if is_file(node):
        print(f"File: {node['name']}, Size: {node['meta']['size']}")
    # elif node["type"] == "directory" and "children" in node:
    elif is_directory(node) and get_children(node):
        for child in node["children"]:
            traverse_tree(child)


# def get_files(node):
#     files = []
#     if is_file(node):
#         files.append({"name": node["name"], "meta" : {"size": node["meta"]["size"] / 2}, "type": node["type"]})
#     elif is_directory(node) and get_children(node):
#         for child in node["children"]:
#             files.extend(get_files(child))
#     return files


def __get_files(node):
    files = []
    if is_file(node):
        file_info = {"name": node["name"], "meta": node["meta"].copy(), "type": node["type"]}

        if file_info["name"].lower().endswith((".jpg", "jpeg", "png")):
            file_info["meta"]["size"] //= 2
        
        files.append(file_info)
    elif is_directory(node) and get_children(node):
        for child in get_children(node):
            files.extend(__get_files(child))
    return files

def compress_images(tree):
    children = get_children(tree)

    def reduce_image_size(node):
        name = get_name(node)
        if not is_file(node) or not name.endswith((".jpg", "jpeg", "png")):
            return node
        new_meta = copy.deepcopy(get_meta(node))
        new_meta["size"] //= 2
        return mkfile(name, new_meta)

    new_children = list(map(reduce_image_size, children))
    return mkdir(get_name(tree), new_children, copy.deepcopy(get_meta(tree)))

# teacher's solution
def _compress_images(tree):
    children = get_children(tree)

    def reduce_image_size(node):
        name = get_name(node)
        if not is_file(node) or not name.endswith('.jpg'):
            return node
        meta = get_meta(node)
        new_meta = copy.deepcopy(meta)
        new_meta['size'] //= 2
        return mkfile(name, new_meta)

    new_children = map(reduce_image_size, children)
    new_meta = copy.deepcopy(get_meta(tree))
    return mkdir(get_name(tree), list(new_children), new_meta)
    
# END


def main():
    tree = mkdir(
        'my documents',
        [
            mkfile('avatar.jpg', {'size': 100}),
            mkfile('photo.jpg', {'size': 150}),
        ],
        {'hide': False}
    )

    print(tree)
    print(compress_images(tree))

    return


if __name__ == "__main__":
    main()


# Реализуйте функцию compress_images(). Она должна принимать на вход директорию, находить внутри нее картинки и уменьшать свойство size в их метаданных в два раза. Функция должна вернуть обновленную директорию со сжатыми картинками и всеми остальными данными, которые были внутри этой директории.

# Картинками считаются все файлы, заканчивающиеся на .jpg:

# from hexlet.fs import mkdir, mkfile
# from solution import compress_images
# tree = mkdir(
#     'my documents',
#     [
#         mkfile('avatar.jpg', {'size': 100}),
#         mkfile('photo.jpg', {'size': 150}),
#     ],
#     {'hide': False}
# )
# compress_images(tree)
# {
#     'name': 'my documents',
#     'type': 'directory',
#     'children': [
#         {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
#         {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
#     ],
#     'meta': {'hide': False},
# }