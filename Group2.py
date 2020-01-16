import csv

_list = list()
list_ = list()
with open('Дорожно-транспортные происшествия за 2018.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for index, row in enumerate(reader):
        if index != 0:
            _list.append([*row, ''])

with open('Соотношение нарушений ПДД на данном аварийном участке и типов жалоб.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index != 0:
            list_.append(row)

with open('Дорожно-транспортные происшествия с рекоммендациями.csv', 'w', newline='', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, delimiter=';',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dictionary = dict()
    for i in range(len(_list)):
        _sh = str('.'.join([str(_list[i][-3]).split('.')[0], str(_list[i][-3]).split('.')[1][:1]]))
        _d = str('.'.join([str(_list[i][-2]).split('.')[0], str(_list[i][-2]).split('.')[1][:1]]))
        for j in range(len(list_)):
            if list_[j][-6] == '(' + ', '.join([_sh, _d]) + ')':
                _list[i][-1] = list_[j][-1]
        writer.writerow(_list[i])
