import csv

_list = list()
list_ = list()
with open('Инициативы граждан за 2018.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index != 0:
            _list.append(row)

with open('Участок ДТП и его характеристики.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index != 0:
            list_.append(row)

with open('Соотношение нарушений ПДД на данном аварийном участке и типов жалоб.csv', 'w', newline='', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, delimiter=';',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dictionary = dict()
    for i in range(len(list_)):
        b = False
        for j in range(len(_list)):
            if list_[i][-5] == _list[j][-1]:
                b = True
                if _list[j][-1] not in dictionary.keys():
                    dictionary[_list[j][-1]] = dict()
                    dictionary[_list[j][-1]][_list[j][3]] = 1
                elif _list[j][3] in dictionary[_list[j][-1]].keys():
                    dictionary[_list[j][-1]][_list[j][3]] += 1
                elif _list[j][3] not in dictionary[_list[j][-1]].keys():
                    dictionary[_list[j][-1]][_list[j][3]] = 1
        if b is True:
            writer.writerow([*list_[i], dictionary[list_[i][-5]]])