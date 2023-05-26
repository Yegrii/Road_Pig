# import json
# from driver_list import keys
#
# # Открываем JSON-файл
# with open('json_files/Race/05.07 MiamiGP/TimingStats.json', encoding='utf-8-sig') as file:
#     data = json.load(file)
#
# # Загрузка key_values из JSON-файла
# with open('json_files/Race/05.07 MiamiGP/KeyValues.json', encoding='utf-8-sig') as file:
#     key_values = json.load(file)
#
#
# # Разбиваем словарь на отдельные переменные
# for key in keys:
#     if key in data['Lines'] or key in key_values:
#         driver_name = key_values[key].get('FirstName') + ' ' + key_values[key].get('LastName')
#         driver_team = key_values[key].get('TeamName')
#         line_data = data['Lines'][key]
#         racing_number = line_data.get('RacingNumber')
#         personal_best_lap_time = line_data.get('PersonalBestLapTime')
#         if racing_number and personal_best_lap_time:
#             lap = personal_best_lap_time.get('Lap')
#             value = personal_best_lap_time.get('Value')
#             print(f"Driver's name: {driver_name}")
#             print(f"Racing Number: {racing_number}")
#             print(f'Team: {driver_team}')
#             print(f"Best lap(_{lap}_) time: {value}")
#             print()
#         else:
#             print(f"Racing Number or Personal Best Lap Time not found for key {key}")
#     else:
#         print(f"Key {key} not found in data['Lines']")
#


# import json
# from driver_list import keys
# from current_race import urls_text
#
#
# # Извлечение названия гонки из ссылки для формирования пути к папке
# end_index = urls_text.find('G', 55)
# race_name = urls_text[55:end_index - 1]
#
# # Открываем JSON-файл
# with open('json_files/Race/MiamiGP/TimingStats.json', encoding='utf-8-sig') as file:
#     data = json.load(file)
#
# # Загрузка key_values из JSON-файла
# with open('json_files/Race/MiamiGP/KeyValues.json', encoding='utf-8-sig') as file:
#     key_values = json.load(file)
#
# output = ""
#
# # Разбиваем словарь на отдельные переменные
# for key in keys:
#     if key in data['Lines'] or key in key_values:
#         driver_name = key_values[key].get('FirstName') + ' ' + key_values[key].get('LastName')
#         driver_team = key_values[key].get('TeamName')
#         line_data = data['Lines'][key]
#         racing_number = line_data.get('RacingNumber')
#         personal_best_lap_time = line_data.get('PersonalBestLapTime')
#         if racing_number and personal_best_lap_time:
#             lap = personal_best_lap_time.get('Lap')
#             value = personal_best_lap_time.get('Value')
#             output += f"{driver_name} {racing_number}\n"
#             # output += f"Racing Number: {racing_number}\n"
#             output += f'Team: {driver_team}\n'
#             output += f"Best time: {value} on lap {lap}\n"
#             output += "\n"
#         else:
#             output += f"Racing Number or Personal Best Lap Time not found for key {key}\n"
#     else:
#         output += f"Key {key} not found in data['Lines']\n"
#
# # Вывод результатов
# print(output)
#
# # Сохранение output в файл
# with open('json_files/Race/MiamiGP/Output.txt', 'w') as file:
#     file.write(output)
#

import json
import os
from driver_list import keys
from current_race import urls_text


# Извлечение названия гонки из ссылки для формирования пути к папке
end_index = urls_text.find('G', 55)
race_name = urls_text[55:end_index - 1]

# Путь к папке с JSON-файлами
json_files_path = f'json_files/Race/{race_name}GP/'

# Путь для сохранения результата
output_file_path = f'json_files/Race/{race_name}GP/Output.txt'

# Открываем JSON-файл
timing_stats_file_path = os.path.join(json_files_path, 'TimingStats.json')
with open(timing_stats_file_path, encoding='utf-8-sig') as file:
    data = json.load(file)

# Загрузка key_values из JSON-файла
key_values_file_path = os.path.join(json_files_path, 'KeyValues.json')
with open(key_values_file_path, encoding='utf-8-sig') as file:
    key_values = json.load(file)

output = ""

# Разбиваем словарь на отдельные переменные
for key in keys:
    if key in data['Lines'] or key in key_values:
        driver_name = key_values[key].get('FirstName') + ' ' + key_values[key].get('LastName')
        driver_team = key_values[key].get('TeamName')
        line_data = data['Lines'][key]
        racing_number = line_data.get('RacingNumber')
        personal_best_lap_time = line_data.get('PersonalBestLapTime')
        if racing_number and personal_best_lap_time:
            lap = personal_best_lap_time.get('Lap')
            value = personal_best_lap_time.get('Value')
            output += f"{driver_name} {racing_number}\n"
            output += f'Team: {driver_team}\n'
            output += f"Best time: {value} on lap {lap}\n"
            output += "\n"
        else:
            output += f"Racing Number or Personal Best Lap Time not found for key {key}\n"
    else:
        output += f"Key {key} not found in data['Lines']\n"

# Вывод результатов
print(output)

# Сохранение output в файл
with open(output_file_path, 'w') as file:
    file.write(output)

