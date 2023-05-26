# import requests
#
# url2 = 'https://livetiming.formula1.com/static/2023/2023-05-07_Miami_Grand_Prix/2023-05-07_Race/TeamRadio' \
#        '/CARSAI01_55_20230507_194512.mp3'
# save_path = 'media/CARSAI01_55_20230507_194512.mp3'  # Замените на путь и имя файла, куда вы хотите сохранить медиафайл
#
# response = requests.get(url2)
# if response.status_code == 200:
#     with open(save_path, 'wb') as file:
#         file.write(response.content)
#     print(f'Saved media file: {save_path}')
# else:
#     print(f'Failed to access URL: {url2}')


import requests
from bs4 import BeautifulSoup

url = 'https://livetiming.formula1.com/static/2023/2023-05-07_Miami_Grand_Prix/2023-05-07_Race/TeamRadio/'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    mp3_links = soup.find_all('a', href=True, class_='mp3')  # Находим все ссылки на mp3 файлы

    for mp3_link in mp3_links:
        file_name = mp3_link['href']
        print(file_name)

else:
    print(f'Failed to access URL: {url}')
