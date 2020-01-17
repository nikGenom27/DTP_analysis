import folium
from folium import plugins, features
import csv
concentration_map = folium.Map(location=[62, 90], zoom_start=4, min_zoom=4)
heat = list()
with open('Дорожнотранспортные происшествия за 2018(урезанные).csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index != 0:
            heading = row
            date = str(int(float(heading[2])))
            mini_data = list(map(float, heading[5:]))
            # print(heading[1], mini_data[-2:])
            stat = sum([int(float(mini_data[0])) * 5, int(float(mini_data[1])) * 2,
                        int(float(mini_data[2])), int(float(mini_data[3]))])
            a = ''.join(['.'.join([date[6:], date[4:6], date[0:4]]),
                  f' В аварии задействовано {int(mini_data[3])} человек(а) и {int(mini_data[2])}' +
                  f' машина / машины / машин. \n' +
                  f'Причиной послужила следующая причина(ы): {heading[4]}.\n'
                  f'Пострадал(о) {int(mini_data[1])}'
                  f' и погиб(ло) {int(mini_data[0])} человек соответственно'])
            # print(a)
            heat.append([mini_data[-2], mini_data[-1], stat])
            if int(mini_data[0]) > 8 or int(mini_data[1]) > 15 or int(mini_data[0]) + int(mini_data[1]) > 10 and\
                    int(mini_data[0]) > 3:
                if heading[1] == 'Столкновение':
                    collision = folium.features.CustomIcon('collision.png', icon_size=(50, 50))
                    folium.Marker(location=[heading[-2], heading[-1]], popup=a, tooltip=heading[1],
                                  icon=collision).add_to(concentration_map)
                elif heading[1] == 'Съезд с дороги':
                    offroad = folium.features.CustomIcon('offroad.png', icon_size=(50, 50))
                    folium.Marker(location=[heading[-2], heading[-1]], popup=a, tooltip=heading[1],
                                  icon=offroad).add_to(concentration_map)
                elif heading[1] == 'Опрокидывание':
                    rollover = folium.features.CustomIcon('rollover.png', icon_size=(50, 50))
                    folium.Marker(location=[heading[-2], heading[-1]], popup=a, tooltip=heading[1],
                                  icon=rollover).add_to(concentration_map)
                else:
                    other = folium.features.CustomIcon('other.png', icon_size=(50, 50))
                    folium.Marker(location=[heading[-2], heading[-1]],
                                  popup=a, tooltip=heading[1], icon=other).add_to(concentration_map)
plugins.HeatMap(heat, name='Концентрация ДТП', min_zoom=1).add_to(concentration_map)
with open('Дорожно-транспортные происшествия с рекомменациями.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index != 0:
            recomend = row[-1]
            cords = [row[-3], row[-2]]
            if recomend != 'Нет рекомендаций' and (int(float(row[-7])) > 5 or int(float(row[-6])) > 10
                                                   or int(float(row[-7])) + int(float(row[-6])) > 6 and int(float(row[-7])) > 2):
                icon = folium.Icon(color='green', icon_color='white', icon='exclamation')
                folium.Marker(location=[cords[-2], cords[-1]],
                              popup=recomend, tooltip='Рекомендация', icon=icon).add_to(concentration_map)
concentration_map.save('MAP.html')
