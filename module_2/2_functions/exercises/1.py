# Использование замыканий в функции.


def id_generator(prefix: str):
    id_database = {}
    def print_id():
        if id_database.get(prefix) != None:
            id_database[prefix] += 1
        else:
            id_database[prefix] = 1
        return(prefix + "-" + f"{id_database[prefix]:03}")
    return print_id


def main():
    user_id = id_generator("USER")
    print(user_id())  # => "USER-001"
    print(user_id())  # => "USER-002"
    print(user_id())

    item_id = id_generator("ITEM")
    print(item_id())  # => "ITEM-001"

if __name__ == "__main__":
    main()


# EXAMPLE
# BEGIN
def id_generator(prefix):
    count = 0

    def generate_id():
        nonlocal count
        count += 1
        return f"{prefix}-{count:03d}"
    return generate_id
# END