# import requests
#
#
# class DataExtraction:
#     def __init__(self, url, save_path, json_file_names):
#         self.url = url
#         self.save_path = save_path
#         self.json_file_names = json_file_names
#
#     def extract_data(self):
#         for file_name in json_file_names:
#             url = url + file_name
#             # Замените на путь и имя файла, куда вы хотите сохранить JSON-файлы
#             save = f'json_files/Race/test/{file_name}'
#
#         response = requests.get(self.url)
#         if response.status_code == 200:
#             with open(self.save_path, 'wb') as file:
#                 file.write(response.content)
#             print(f'Saved JSON file: {self.save_path}')
#         else:
#             print(f'Failed to access URL: {self.url}')
#
#
# url = 'https://livetiming.formula1.com/static/2023/2023-04-02_Australian_Grand_Prix/2023-04-02_Race/'
#
# json_file_names = ['TimingStats.json', 'ChampionshipPrediction.json', 'DriverList.json', 'RaceControlMessages.json',
#                    'RaceControlMessages.json', 'SessionInfo.json', 'TeamRadio.json', 'TimingAppData.json',
#                    'TimingData.json']
#
# save_path = 'json_files/Race/test/'
#
#
# data_extraction = DataExtraction(url, save_path, json_file_names)
# data_extraction.extract_data()


import requests
from current_race import urls_text
import os


# Скачивание json файлов с сайта для извлечения данных из них
# Название необходимых json файлов можно найти в переменной json_file_names
class DataExtraction:
    # url - ссылка на json файлы
    # save_path - путь к папке, куда будут сохранены json файлы
    # json_files - список названий json файлов
    def __init__(self, url, save_path, json_files):
        self.url = url
        self.save_path = save_path
        self.json_files = json_files

    def extract_data(self):
        # Скачивание json файлов с сайта и сохранение их
        for file_name in self.json_files:
            file_url = self.url + file_name
            file_save_path = self.save_path + file_name
            response = requests.get(file_url)
            if response.status_code == 200:
                with open(file_save_path, 'wb') as file:
                    file.write(response.content)
                print(f'Saved JSON file: {file_save_path}')
            else:
                print(f'Failed to access URL: {file_url}')


# Ссылка на json файлы
json_file_names = ['TimingStats.json', 'ChampionshipPrediction.json', 'DriverList.json', 'RaceControlMessages.json',
                   'RaceControlMessages.json', 'SessionInfo.json', 'TeamRadio.json', 'TimingAppData.json',
                   'TimingData.json']

# Извлечение названия гонки из ссылки для формирования пути к папке
end_index = urls_text.find('G', 55)
race_name = urls_text[55:end_index - 1]

# Формирование пути к папке, используя название гонки
path = f'json_files/Race/{race_name}GP/'

# Проверка наличия папки и создание ее, если она не существует
if not os.path.exists(path):
    os.makedirs(path)

# Создание экземпляра класса DataExtraction и вызов метода extract_data()
data_extraction = DataExtraction(urls_text, path, json_file_names)
data_extraction.extract_data()
