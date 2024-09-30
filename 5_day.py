# Функция для вычисления периметра куба.
def calc_cube_perimeter(side):
    return side * 12

# Вызов функции calc_cube_perimeter() с аргументом 3
one_cube_perimeter = calc_cube_perimeter(3)
full_length = one_cube_perimeter * 8
print('Необходимый метраж палок для 8 кубов:', full_length)

# Функция для вычисления площади куба.
def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area

# Вызов функции calc_cube_area() с аргументом 3
one_cube_area = calc_cube_area(3)
full_area = one_cube_area * 8
print('Необходимая площадь стекла для 8 кубов, кв.м:', full_area)




# Функция для вычисления периметра куба.
def calc_cube_perimeter(side):
    return side * 12

# Функция для вычисления площади куба.
def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area

# Основная функция, которая принимает длину ребра куба
def calc_cube(side):
    # Вызываем функцию, рассчитывающую периметр
    # и передаём в неё размер куба
    one_cube_perimeter = calc_cube_perimeter(side)
    full_length = one_cube_perimeter * 8

    # Вызываем функцию, рассчитывающую площадь стекла
    # и передаём в неё размер куба
    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * 8

    print('Для 8 кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)

# В результате остался лишь один вызов "основной" функции,
# а она уже вызовет две вспомогательные
calc_cube(3)




def multiplication(multiplier_1, multiplier_2):
    print(multiplier_1 * multiplier_2)

# Дальше начинается код, который расположен вне функции:
# Python понимает это по отсутствию отступов.

# Вызов функции multiplication()
multiplication(7, 6)