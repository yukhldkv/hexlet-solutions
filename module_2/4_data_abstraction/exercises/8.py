import math


def make(numer, denom):
    if denom == 0:
        raise ValueError("Denominator cannot be zero")
    
    gcd = math.gcd(numer, denom)
    numer //= gcd
    denom //= gcd
    return {
        "numer": numer, 
        "denom": denom
    }


def get_numer(rational):
    return rational["numer"]


def get_denom(rational):
    return rational["denom"]


def add(rational1, rational2):
    return make(get_denom(rational2) * get_numer(rational1) + get_denom(rational1) * get_numer(rational2), get_denom(rational1) * get_denom(rational2))


def sub(rational1, rational2):
    return make(get_denom(rational2) * get_numer(rational1) - get_denom(rational1) * get_numer(rational2), get_denom(rational1) * get_denom(rational2))

def main():
    rat1 = make(3, 9)
    print(get_numer(rat1))  # 1
    print(get_denom(rat1))  # 3
    rat2 = make(10, 3)
    rat3 = add(rat1, rat2)
    print(to_str(rat3))  # 11/3
    rat4 = sub(rat1, rat2)
    print(to_str(rat4))  # -3/1
    return


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"


if __name__ == "__main__":
    main()


# Реализуйте абстракцию для работы с рациональными числами, которая включает в себя следующие функции:

# Конструктор make — принимает на вход числитель и знаменатель, возвращает дробь
# Селектор get_numer — возвращает числитель
# Селектор get_denom — возвращает знаменатель
# Сложение add — складывает переданные дроби
# Вычитание sub — находит разность между двумя дробями
# Не забудьте реализовать нормализацию дробей удобным для вас способом.

# Примеры работы:

# import rational

# rat1 = rational.make(3, 9)
# rational.get_numer(rat1)  # 1
# rational.get_denom(rat1)  # 3
# rat2 = rational.make(10, 3)
# rat3 = rational.add(rat1, rat2)
# rational.to_str(rat3)  # 11/3
# rat4 = rational.sub(rat1, rat2)
# rational.to_str(rat4)  # -3/1
# Подсказки
# Приведение дробей к единому знаменателю
# Функция gcd из модуля math находит наибольший общий делитель двух чисел
# Функция to_str возвращает строковое представление числа (используется для отладки)
# Функция int преобразует значение к целому числу