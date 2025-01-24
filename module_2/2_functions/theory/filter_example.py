def my_filter(callback, collection):
  for item in collection:
    # Предикат используется только для проверки
    # Внутрь callback по очереди передается каждый элемент коллекции collection
    if callback(item):
      # Реализуем ленивость
      yield item

users = [
  { 'name': 'Igor', 'age': 19 },
  { 'name': 'Danil', 'age': 1 },
  { 'name': 'Vovan', 'age': 4 },
  { 'name': 'Matvey', 'age': 16 },
]

filtered_users = my_filter(lambda user: user['age'] > 10, users)
list(filtered_users) # [{'name': 'Igor', 'age': 19}, {'name': 'Matvey', 'age': 16}]

# see exercise 13.py

# fiter это фильтрация по определённому признаку

# reduce это агрегация по определённому признаку