import requests
import os
from driver_list import keys, data

# Путь для сохранения изображений
save_directory = 'media/pic'

# Проверка наличия папки и создание, если её нет
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Скачивание изображений и сохранение их
for key in keys:
    reference = data[key]['Reference']
    url = f'https://media.formula1.com/content/dam/fom-website/2018-redesign-assets/drivers/2023/{reference}.png.transform/2col-retina/image.png'

    # Определение имени файла на основе reference
    file_name = f'{key}.webp'
    # Полный путь для сохранения файла
    save_path = os.path.join(save_directory, file_name)

    # Загрузка изображения по URL
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f'Saved image: {save_path}')
    else:
        print(f'Failed to download image from URL: {url}')
