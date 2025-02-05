def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None


# from points import get_quadrant, get_x, get_y, make_decart_point


def make_rectangle(point, width, height):
    return {
        "start_point": point,
        "width": width,
        "height": height
    }


def get_start_point(rectangle):
    return rectangle["start_point"]


def get_width(rectangle):
    return rectangle["width"]


def get_height(rectangle):
    return rectangle["height"]


def contains_origin(rectangle):
    top_left = get_start_point(rectangle)
    top_right = make_decart_point(get_x(top_left) + get_width(rectangle), get_y(top_left))
    bottom_left = make_decart_point(get_x(top_left), get_y(top_left) - get_height(rectangle))
    bottom_right = make_decart_point(get_x(top_right), get_y(bottom_left))
    coordinates = {get_quadrant(top_left), get_quadrant(top_right), get_quadrant(bottom_left), get_quadrant(bottom_right)}
    # check if rectangle points are in different quadrants
    return True if len(coordinates) == 4 else False


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)
    if x >= 0 and y >= 0:
        return 1
    if x <= 0 and y >= 0:
        return 2
    if x <= 0 and y <= 0:
        return 3
    if x >= 0 and y <= 0:
        return 4


def main():
    p = make_decart_point(0, 1)
    rectangle = make_rectangle(p, 4, 5)
    rectangle2 = make_rectangle(make_decart_point(-4, 3), 5, 4)
    print(contains_origin(rectangle))
    print(contains_origin(rectangle2))
    return

if __name__ == "__main__":
    main()


# Реализуйте абстракцию (набор функций) для работы с прямоугольниками, стороны которого всегда параллельны осям. Прямоугольник может располагаться в любом месте координатной плоскости.

# При такой постановке достаточно знать только три параметра для однозначного задания прямоугольника на плоскости: координаты левой верхней точки, ширину и высоту. Зная их, мы всегда можем построить прямоугольник одним способом.

#       Y
#       |
#     4 |    точка   ширина
#       |       *-------------
#     3 |       |            |
#       |       |            | высота
#     2 |       |            |
#       |       --------------
#     1 |
#       |
# ------|--------------------------- X
#     0 |  1   2   3   4   5   6   7
#       |
#       |
#       |
# Основной интерфейс:

# make_rectangle() (конструктор) — создает прямоугольник. Принимает параметры: левую верхнюю точку, ширину и высоту. Ширина и высота – положительные числа
# Селекторы get_start_point(), get_width() и get_height()
# contains_origin() — проверяет, принадлежит ли центр координат прямоугольнику. То есть не лежит на границе прямоугольника, а находится внутри. Чтобы в этом убедиться, достаточно проверить, что все вершины прямоугольника лежат в разных квадрантах. Их можно высчитать в момент проверки
# # Создание прямоугольника:
# # p - левая верхняя точка
# # 4 - ширина
# # 5 - высота
# #
# # p    4
# # -----------
# # |         |
# # |         | 5
# # |         |
# # -----------

# p = make_decart_point(0, 1)
# rectangle = make_rectangle(p, 4, 5)

# contains_origin(rectangle)  # False

# rectangle2 = make_rectangle(make_decart_point(-4, 3), 5, 4)
# contains_origin(rectangle2)  # True
# Подсказки
# Квадрант плоскости — любая из четырех областей или углов, на которые плоскость делится двумя взаимно перпендикулярными прямыми, принятыми в качестве осей координат

# Для определения квадранта, в которой лежит точка, используйте функцию get_quadrant():

# point_1 = make_decart_point(2, 3)
# point_2 = make_decart_point(-2, -3)
# get_quadrant(point_1)  # 1
# get_quadrant(point_2)  # 3