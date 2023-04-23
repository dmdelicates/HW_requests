print('1 задание')
import requests
import json
from pprint import pprint
url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)

name_hero = ['Hulk', 'Captain America', 'Thanos']
smart_hero = ''
top_intellect = 0
for super_hero in resp.json():
    if super_hero['name'] in name_hero:
       if super_hero['powerstats']['intelligence'] > top_intellect:
           smart_hero = super_hero['name']
           top_intellect = super_hero['powerstats']['intelligence']
           print(super_hero['name'], super_hero['powerstats']['intelligence'])
print(f'Самый умный супергерой {smart_hero} с интеллектом {top_intellect}')

print('2 задание')

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get('href')
        print(href)
        return href

    def upload(self, file_path: str):
        href = self._get_upload_link(disk_file_path=file_path)
        response = requests.put(href, data=open(file_path, 'rb'))
        if response.status_code == 201:
            print("Success")
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '1.txt'
    token = 'y0_AgAEA7qhPt6WAADLWwAAAADhoAWIlGHQIiv-TqyJnuvX5OBWN3TZFQA'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


