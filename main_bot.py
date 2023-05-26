import requests
import subprocess
import os
from telegram_token import TOKEN

# Получение текущего пути
current_path = os.path.dirname(os.path.abspath(__file__))

# Полный путь к файлу driver_list.py
driver_list_path = os.path.join(current_path, 'driver_list.py')

# Путь к файлу с изображением
image_path = 'media/pic/1.webp'

# token/ID бота и чата в Telegram
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
chat_id = "-1001983169778"
print(requests.get(url).json())


# Запуск файла driver_list.py
subprocess.run(['python', 'driver_list.py'], check=True)

# Запуск файла timing_stats.py
subprocess.run(['python', 'timing_stats.py'], check=True)


# Чтение output из файла
with open('json_files/Race/MiamiGP/Output.txt', 'r') as file:
    output = file.read()

# Отправка изображения с прозрачным фоном в канал как документ возможна только если расширение файла .webp
url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
data = {
    'chat_id': chat_id
}
files = {
    'document': open(image_path, 'rb')
}
response_img = requests.post(url, data=data, files=files)
print(response_img.json())

# Отправка сообщения в Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    'chat_id': chat_id,
    'text': output
}
response_text = requests.post(url, json=data)
print(response_text.json())
