# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def main():
    number = int(input('Введите число:'))
    print(list_of_natural_divisors(number))


def list_of_natural_divisors(number):
    list_nat = []
    for i in range(2, number+1):
        if number / i == int(number / i):
            k = 0
            for j in range(2, i // 2+1):
                if (i % j == 0):
                    k += 1
            if k == 0:
                list_nat.append(i)
    return list_nat


if __name__ == '__main__':
    main()
