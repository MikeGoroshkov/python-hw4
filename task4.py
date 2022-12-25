# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def main():
    max_degree = int(input('Введите максимальную степень полинома:'))
    polynom = get_polynom(max_degree)
    print(polynom)
    with open('file.txt', 'w') as data:
        data.write(polynom)


def get_polynom(max_degree):
    polinom = ''
    coef_list = [random.randint(0, 100) for _ in range(max_degree+1)]
    degree = max_degree
    for coef in coef_list:
        if coef == 0 and degree <= 0:
            polinom += f' = 0'
        elif coef != 0:
            if degree < max_degree:
                polinom += ' + '
            if degree > 0:
                if coef == 1:
                    polinom += f'x^{degree}'
                else:
                    polinom += f'{coef}*x^{degree}'
            else:
                polinom += f'{coef} = 0'
        degree -= 1
    return polinom


if __name__ == '__main__':
    main()
