# BEGIN (write your solution here)
def update_inventory(inventory: dict, item: str, count: int):
    inventory[item] = inventory.get(item, 0) + count

def get_stock(inventory: dict, item: str) -> int:
    return inventory.get(item, 0)
# END


def main():
    inventory = {}
    update_inventory(inventory, "pear", 10)
    print(inventory)


if __name__ == "__main__":
    main()


# Реализуйте функцию update_inventory(), которая принимает инвентарь, именование и количество товара и добавляет к нему количество товара в инвентаре. Если товара нет в инвентаре, функция должна добавить его с указанным количеством.

# Также реализуйте функцию get_stock(), которая принимает инвентарь и имя товара и возвращает текущее количество указанного товара в инвентаре. Если товара нет, возвращает 0.

# Убедитесь, что обе функции следуют принципу разделения команд и запросов (CQS).

# Пример использования:

# inventory = {}
# update_inventory(inventory, "apple", 10)
# print(get_stock(inventory, "apple"))  # => 10
# update_inventory(inventory, "banana", 5)
# print(get_stock(inventory, "banana"))  # => 5
# update_inventory(inventory, "banana", 2)
# print(get_stock(inventory, "banana"))  # => 7