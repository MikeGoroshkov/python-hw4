# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def main():
    data_1 = open('file_1.txt', 'r')
    pol_1 = data_1.readline()
    data_1.close()
    data_2 = open('file_2.txt', 'r')
    pol_2 = data_2.readline()
    data_2.close()
    dict_1 = get_coef_dict(pol_1)
    dict_2 = get_coef_dict(pol_2)
    dict_sum = sum_value_dictionaries(dict_1, dict_2)
    poly = get_polynom(dict_sum)
    with open('file_3.txt', 'w') as data:
        data.write(poly)


def get_coef_dict(polynom):
    dict = {}
    p_s = polynom.split(' + ')
    dict_0 = int(p_s[len(p_s)-1].replace(' = 0', ''))
    p_s.pop(len(p_s)-1)
    for i in p_s:
        i_s = i.split('*x^')
        if 'x^' in ''.join(i_s):
            dict[int(''.join(i_s)[2:])] = 1
        else:
            dict[int(i_s[1])] = int(i_s[0])
    dict[0] = dict_0
    return dict


def sum_value_dictionaries(dict_1, dict_2):
    resultdict = dict_1
    for key in dict_2:
        try:
            resultdict[key] += dict_2[key]
        except KeyError:
            resultdict[key] = dict_2[key]
    return dict(sorted(resultdict.items(), key=lambda x: -x[0]))


def get_polynom(dic):
    polinom = ''
    max_degree = max(dic.keys())
    degree = max_degree
    for coef in dic.values():
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
