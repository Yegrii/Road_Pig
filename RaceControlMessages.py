import json

# Открываем JSON-файл
with open('json_files/Race/MiamiGP/RaceControlMessages.json', encoding='utf-8-sig') as file:
    data = json.load(file)

print(data)

RCM_keys = ['Lap', 'Flag', 'Message']

extracted_values = [{key: item.get(key) for key in RCM_keys} for item in data['Messages']]

print()
print(extracted_values)
