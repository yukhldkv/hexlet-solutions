# from points import get_x, get_y, make_decart_point


def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def make_segment(point0, point1):
    return {"p0": point0, "p1": point1}


def get_mid_point_of_segment(segment):
    x0, y0 = get_x(segment["p0"]), get_y(segment["p0"])
    x1, y1 = get_x(segment["p1"]), get_y(segment["p1"])
    return {"x": (x1 + x0) / 2, "y": (y1 + y0) / 2}


def get_begin_point(segment):
    return segment["p0"]


def get_end_point(segment):
    return segment["p1"]


def main():
    segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
    print(get_begin_point(segment))  # {'x': 3, 'y': 2}
    print(get_end_point(segment))  # {'x': 0, 'y': 0}
    print(get_mid_point_of_segment(segment))  # {'x': 1.5, 'y': 1}
    return

if __name__ == "__main__":
    main()

# Отрезок — еще один графический примитив. В коде описывается парой точек, одна из которых — начало отрезка, другая — конец. Обычный отрезок не имеет направления, поэтому вы сами можете выбирать, какую точку считать началом, а какую - концом.

# В этом задании подразумевается, что вы уже понимаете принцип построения абстракции. Вы способны самостоятельно принять решение о том, как она будет реализована. Сделать это можно разными способами и нет одного правильного.

# src/segments.py
# Реализуйте указанные ниже функции:

# make_segment() — принимает на вход две точки и возвращает отрезок
# get_mid_point_of_segment() — принимает на вход отрезок и возвращает точку, которая находится на середине отрезка
# get_begin_point() — принимает на вход отрезок и возвращает точку начала отрезка
# get_end_point() — принимает на вход отрезок и возвращает точку конца отрезка
# Представление отрезка вы должны придумать сами.

# Пример работы:

# from points import make_decart_point

# segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
# # В примерах ниже возвращаются точки с координатами (x, y)
# get_begin_point(segment)  # {'x': 3, 'y': 2}
# get_end_point(segment)  # {'x': 0, 'y': 0}
# get_mid_point_of_segment(segment)  # {'x': 1.5, 'y': 1}
# Подсказки
# Для создания точек используйте функцию make_decart_point()