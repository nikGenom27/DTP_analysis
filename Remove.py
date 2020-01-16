import csv

l = list()
with open('инициатива граждан.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for index, row in enumerate(reader):
        l.append([])
        for i in range(len(row)):
            if i != 10 and i != 9 and i != 8 and i != 1 and i != 2 and i != 3:
                l[-1].append(row[i])
print(len(l[581]))
print(len(l[0]))
with open('Дорожнотранспортные происшествия за 2018(урезанные).csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(l)):
        writer.writerow([*l[i]])