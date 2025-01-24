def rgb(red=0, green=0, blue=0):
    return f'rgb({red}, {green}, {blue})'


# BEGIN (write your solution here)
def get_colors() -> dict:
    colors = {}
    colors.setdefault("red", rgb(red = 255))
    colors.setdefault("green", rgb(green = 255))
    colors.setdefault("blue", rgb(blue = 255))
    return colors
# END

# В этом упражнении вам нужно будет реализовать функцию get_colors(), которая должна вернуть словарь цветов, используя функцию rgb(). Функция rgb() уже реализована в упражнении. В словаре должны присутствовать ключи 'red', 'green', 'blue'. Каждому ключу должен соответствовать результат вызова функции rgb() со значением 255 для соответствующего ключу аргумента. Для построения каждого цвета используйте только один аргумент!

# О цветовой модели RGB вы можете почитать тут

# colors = get_colors()
# colors.keys() 
# # dict_keys(['red', 'green', 'blue'])
# colors['red'] 
# # 'rgb(255, 0, 0)'
# colors['blue'] 
# # 'rgb(0, 0, 255)'