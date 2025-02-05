import math


def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


def get_x(point):
    return math.trunc(point["radius"] * math.cos(point["angle"])) # нарушает абстракцию, правильно получить значение через селектор


def get_y(point):
    return math.trunc(point["radius"] * math.sin(point["angle"])) # нарушает абстракцию, правильно получить значение через селектор


def main():
    point = make_point(4, 8)
    print(get_x(point))  # 4
    print(get_y(point))  # 8
    return

if __name__ == "__main__":
    main()


# Реализуйте интерфейсные функции точек:

# make_point() — принимает на вход координаты и возвращает точку, уже реализован
# get_x()
# get_y()
# x = 4
# y = 8

# # point хранит в себе данные в полярной системе координат
# point = make_point(x, y)

# # Здесь происходит преобразование из полярной в декартову
# get_x(point)  # 4
# get_y(point)  # 8
# Подсказки
# Трансляция декартовых координат в полярные была описана в теории
# Получить x можно по формуле radius * cos(angle)
# Получить y можно по формуле radius * sin(angle)