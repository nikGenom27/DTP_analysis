import os
import sys

import pygame
import requests

geocoder_request = '''http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Кемерово,%20проспект%20Ленинградский,%2021&format=json'''

# Выполняем запрос.
response = requests.get(geocoder_request)
if response:
    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    # Согласно описанию ответа, он находится по следующему пути:
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Полный адрес топонима:
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Печатаем извлечённые из ответа поля:
    print(toponym_coodrinates)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")

response = None
map_request = f"http://static-maps.yandex.ru/1.x/?ll={','.join(str(toponym_coodrinates).split())}&spn=0.002,0.002&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
