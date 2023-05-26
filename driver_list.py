# # Description: Извлечение данных из JSON-файла с информацией о гонщиках и командах в текущем сезоне Формулы-1.
# import json
# from current_race import urls_text
#
# # Извлечение названия гонки из ссылки для формирования пути к папке
# end_index = urls_text.find('G', 55)
# race_name = urls_text[55:end_index - 1]
#
# # Открываем JSON-файл
# with open('json_files/Race/Saudi_ArabianGP/DriverList.json', encoding='utf-8-sig') as file:
#     data = json.load(file)
#
# # Разбиваем словарь на отдельные переменные
# for key, value in data.items():
#     locals()[key] = value
#
#
# # Получение всех ключей главного словаря
# keys = list(data.keys())
#
# # Ключи, которые должны быть в словаре для каждого гонщика
# required_keys = ['TeamName', 'FirstName', 'LastName']
#
# # Словарь для хранения ключей и значений
# key_values = {}
#
#
# # Вывод содержимого для нужного ключа
# important_keys = ['RacingNumber', 'Tla', 'TeamName', 'TeamColour', 'FirstName', 'LastName', 'Reference', 'CountryCode']
#
# # Ключ для изображения гонщика
# pic_url = ['HeadshotUrl']
#
# # Ключи, которые должны быть в словаре для каждого гонщика
# if __name__ == '__main__':
#     for key in keys:
#         content = data[key]
#         print(f"Driver number {key}:")
#         print(content)
#         print()  # Пустая строка для разделения вывода
#
#     # Выборка данных по ключам из словаря important_keys
#     for i in keys:
#         if i in data:
#             extracted_data = {key: data[i].get(key) for key in important_keys}
#             print(extracted_data)
#         else:
#             print(f"Ключ {i} не найден в словаре.")
#
#     # Выборка данных по ключам из словаря required_keys
#     for key in keys:
#         if key in data:
#             values = {}
#             for required_key in required_keys:
#                 if required_key in data[key]:
#                     value = data[key][required_key]
#                     values[required_key] = value
#                 else:
#                     print(f"Required key '{required_key}' not found in the dictionary for key '{key}'")
#             key_values[key] = values
#         else:
#             print(f"Key '{key}' not found in the dictionary")
#
#     # Сохранение key_values в JSON-файл
#     with open('json_files/Race/Saudi_ArabianGP/KeyValues.json', 'w') as file:
#         json.dump(key_values, file)
#



import json
import os
from current_race import urls_text

# Извлечение названия гонки из ссылки для формирования пути к папке
end_index = urls_text.find('G', 55)
race_name = urls_text[55:end_index - 1]

# Путь к папке с JSON-файлами
json_files_path = f'json_files/Race/{race_name}GP/'

# Открываем JSON-файл
driver_list_file_path = os.path.join(json_files_path, 'DriverList.json')
with open(driver_list_file_path, encoding='utf-8-sig') as file:
    data = json.load(file)

# Разбиваем словарь на отдельные переменные
for key, value in data.items():
    locals()[key] = value

# Получение всех ключей главного словаря
keys = list(data.keys())

# Ключи, которые должны быть в словаре для каждого гонщика
required_keys = ['TeamName', 'FirstName', 'LastName']

# Словарь для хранения ключей и значений
key_values = {}


# Вывод содержимого для нужного ключа
important_keys = ['RacingNumber', 'Tla', 'TeamName', 'TeamColour', 'FirstName', 'LastName', 'Reference', 'CountryCode']

# Ключ для изображения гонщика
pic_url = ['HeadshotUrl']

# Ключи, которые должны быть в словаре для каждого гонщика
if __name__ == '__main__':
    for key in keys:
        content = data[key]
        print(f"Driver number {key}:")
        print(content)
        print()  # Пустая строка для разделения вывода

    # Выборка данных по ключам из словаря important_keys
    for i in keys:
        if i in data:
            extracted_data = {key: data[i].get(key) for key in important_keys}
            print(extracted_data)
        else:
            print(f"Ключ {i} не найден в словаре.")

    # Выборка данных по ключам из словаря required_keys
    for key in keys:
        if key in data:
            values = {}
            for required_key in required_keys:
                if required_key in data[key]:
                    value = data[key][required_key]
                    values[required_key] = value
                else:
                    print(f"Required key '{required_key}' not found in the dictionary for key '{key}'")
            key_values[key] = values
        else:
            print(f"Key '{key}' not found in the dictionary")

    # Путь для сохранения файла с key_values
    key_values_file_path = os.path.join(json_files_path, 'KeyValues.json')

    # Сохранение key_values в JSON-файл
    with open(key_values_file_path, 'w') as file:
        json.dump(key_values, file)

