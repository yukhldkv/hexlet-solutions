def my_map(callback, collection):
  for item in collection:
    # Вызов переданного колбека на каждом элементе коллекции
    new_item = callback(item)
    # Сделаем нашу функцию тоже ленивой с помощью yield
    yield new_item


def main():
    numbers = [5, 2, 3]
    new_numbers = my_map(lambda number: number ** 2, numbers)
    print(list(new_numbers)) # [25, 4, 9]


if __name__ == "__main__":
    main()

# look exercie 12.py

# map это отображение по определённому признаку