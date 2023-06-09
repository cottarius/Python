import math
from statistics import mean

def bmi(weight, height):  # Функция для подсчета индекса массы тела с входными параметрами {вес} и {рост}
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "UnderWeight"
    elif 18.5 < bmi <= 25.0:
        return "Normal"
    elif 25.0 < bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"


def abbrev_name(name): # Функция конвертации имени и фамилии в инциалы с точкой между инициалами
    list = name.split(" ")
    new_list = []
    for i in list:
        new_list.append(i[0].upper())
    return ".".join(new_list)


def simple_multiplication(number):  # Если число чётное, то умножаем на 8. Если нечётное, то умножаем на 9
    # return number * 9 if number % 2 else number * 8
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9


def square_sum(numbers):  # Вычисление суммы квадратов из элементов списка
    # return sum(i ** 2 for i in numbers)
    summ = 0
    for i in numbers:
        summ += i ** 2
    return summ


def better_than_average(class_points, your_points):
    return True if your_points > mean(class_points) else False


def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


def paperwork(n, m):
    return n * m if n >= 0 and m >= 0 else 0


def string_to_array(s): # разбивание строки на отдельные слова
    return s.split(" ")


def reverse_seq(n): # возвращает массив интов от n до 1
    lst = []
    for i in range(n, 0, -1):
        lst.append(i)
    return lst
    # return list(range(n, 0, -1))


def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


def sum_array(a):
    return sum(a) if len(a) > 0 else 0


def find_smallest_int(arr):
    return min(arr)


print(bmi(50, 1.80))
print(abbrev_name('Sam Harris'))
print(simple_multiplication(2))
print(square_sum([0, 3, 4, 5]))
print(better_than_average([2, 3], 5))
