# Вычислить число c заданной точностью d
#     Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


def main():
    number = float(input('Введите число: '))
    precision = float(input('Введите точность числа: '))
    print(get_number_with_precision(number, precision))


def get_number_with_precision(number, precision):
    float_digits = -1
    while int(1/precision) != 0:
        precision *= 10
        float_digits += 1
    return round(number, float_digits)


if __name__ == '__main__':
    main()
