import csv

rows = list()
top_list = list()
low_list = list()
index = int()
with open('Дорожно-транспортные происшествия с рекомменациями.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for i, j in enumerate(reader):
        rows.append(j[:-1])
        top_list.append([])
        low_list.append([])
        if len(j[-1]) != 0:
            a = j[-1][1:-1].split(', ')
            b = int()
            for x in range(len(a)):
                b += int(a[x].split(': ')[1])
                a[x] = a[x].split(': ')
            for y in range(len(a)):
                if int(a[y][1]) >= b // 2:
                    top_list[i].append(a[y][0])
                else:
                    low_list[i].append(a[y][0])
        index = i + 1
with open('Дорожно-транспортные происшествия с рекомменациями.csv', 'w', newline='', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, delimiter=';',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(index):
        if len(top_list[i]) != 0 and len(low_list[i]) != 0:
            writer.writerow([*rows[i], 'Настоятельно рекомендуем исправить: ' + ', '.join(
                top_list[i]) + ' Стоит обратить внимание: ' + ', '.join(low_list[i])])
        elif len(top_list[i]) != 0 and len(low_list[i]) == 0:
            writer.writerow([*rows[i], 'Настоятельно рекомендуем исправить: ' + ', '.join(top_list[i])])
        elif len(top_list[i]) == 0 and len(low_list[i]) != 0:
            writer.writerow([*rows[i], 'Стоит обратить внимание: ' + ', '.join(low_list[i])])
        else:
            writer.writerow([*rows[i], 'Нет рекомендаций'])
