def get_mid_point(point1, point2):
    x1, y1 = float(point1['x']), float(point1['y'])
    x2, y2 = float(point2['x']), float(point2['y'])
    return {'x': (x1 + x2) / 2, 'y': (y1 + y2) / 2}


def get_mid_point(point1, point2):
    (x1, y1), (x2, y2) = map(lambda p: map(float, p.values()), (point1, point2))
    return {'x': (x1 + x2) / 2, 'y': (y1 + y2) / 2}


from operator import itemgetter

def get_mid_point(point1, point2):
    get_xy = itemgetter('x', 'y')  # Extracts 'x' and 'y' values
    x1, y1 = map(float, get_xy(point1))
    x2, y2 = map(float, get_xy(point2))

    return {'x': (x1 + x2) / 2, 'y': (y1 + y2) / 2}