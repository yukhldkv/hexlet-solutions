# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))


# def create_factorial():
#     def inner(n):
#         if n <= 1:
#             return 1
#         return n * inner(n - 1)
#     return inner

# closure_factorial = create_factorial()
# # print(closure_factorial(5))


# from collections import defaultdict

# def nested_dict():
#     return defaultdict(nested_dict)

# catalog = nested_dict()
# catalog['Electronics']['Mobile Phone']['Smartphone']['Items'] = []
# catalog['Electronics']['Mobile Phone']['Smartphone']['Items'].append('Apple Smartphone')
# catalog['Electronics']['Mobile Phone']['Smartphone']['Items'].append('Google Smartphone')

# def to_regular_dict(default_dict):
#     if isinstance(default_dict, defaultdict):
#         new_dict = {}
#         for key, value in default_dict.items():
#             new_dict[key] = to_regular_dict(value)
#         default_dict = new_dict
#     elif isinstance(default_dict, dict):
#         new_dict = {}
#         for key, value in default_dict.items():
#             new_dict[key] = to_regular_dict(value)
#         default_dict = new_dict
#     elif isinstance(default_dict, list):
#         new_list = []
#         for item in default_dict:
#             new_list.append(to_regular_dict(item))
#         default_dict = new_list
#     return default_dict


# dict_catalog = to_regular_dict(catalog)
# print(dict_catalog)


from collections import defaultdict

def nested_dict():
    return defaultdict(nested_dict)


def to_regular_dict(default_dict):
    if isinstance(default_dict, defaultdict):
        new_dict = {}
        for key, value in default_dict.items():
            new_dict[key] = to_regular_dict(value)
        default_dict = new_dict
    elif isinstance(default_dict, dict):
        new_dict = {}
        for key, value in default_dict.items():
            new_dict[key] = to_regular_dict(value)
        default_dict = new_dict
    elif isinstance(default_dict, list):
        new_list = []
        for item in default_dict:
            new_list.append(to_regular_dict(item))
        default_dict = new_list
    return default_dict


def _print_catalog(data, path = ""):
    if not isinstance(data, dict):
        print(data)
        return

    for key, value in data.items():
        new_path = f"{path} - {key}" if path else key
        if key.lower() == 'items' and isinstance(value, list):
            print(f"{new_path}:")
            for item in value:
                print(f'- {item}')
        else:
            _print_catalog(value, new_path)


def print_catalog(data, depth = 0):
    if not isinstance(data, dict):
        print(data)
        return
    for key, value in data.items():
        if key.lower() == 'items' and isinstance(value, list):
            for item in value:
                print(" " * depth, f'- {item}')
        else:
            print(" " * depth, f'{key}')
            print_catalog(value, depth + 1)


from create_catalog import create_structure
catalog = nested_dict()
catalog = create_structure(catalog)
print_catalog(to_regular_dict(catalog))