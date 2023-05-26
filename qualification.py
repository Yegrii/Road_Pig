# # Current Race URL
# import datetime
#
# urls_q_dict = {
#              '03.05': {'https://livetiming.formula1.com/static/2023/2023-03-05_Bahrain_Grand_Prix/2023-03-05_Race/'},
#              '03.19': {'https://livetiming.formula1.com/static/2023/2023-03-19_Saudi_Arabian_Grand_Prix/2023-03'
#                        '-19_Race/'},
#              '04.02': {'https://livetiming.formula1.com/static/2023/2023-04-02_Australian_Grand_Prix/2023-04-02_Race/'},
#              '05.24': {'https://livetiming.formula1.com/static/2023/2023-04-30_Azerbaijan_Grand_Prix/2023-04-30_Race/'},
#              '05.07': {'https://livetiming.formula1.com/static/2023/2023-05-07_Miami_Grand_Prix/2023-05-07_Race/'},
#              '05.28': {'https://livetiming.formula1.com/static/2023/2023-05-28_Monaco_Grand_Prix/2023-05-28_Race/'},
#              '06.04': {'https://livetiming.formula1.com/static/2023/2023-06-04_Spain_Grand_Prix/2023-06-04_Race/'},
#              '06.18': {'https://livetiming.formula1.com/static/2023/2023-06-18_Canada_Grand_Prix/2023-06-18_Race/'},
#              '07.02': {'https://livetiming.formula1.com/static/2023/2023-07-02_Austrian_Grand_Prix/2023-07-02_Race/'},
#              '07.09': {'https://livetiming.formula1.com/static/2023/2023-07-09_British_Grand_Prix/2023-07-09_Race/'},
#              '07.23': {'https://livetiming.formula1.com/static/2023/2023-07-23_Hungarian_Grand_Prix/2023-07-23_Race/'},
#              '07.30': {'https://livetiming.formula1.com/static/2023/2023-07-30_Belgian_Grand_Prix/2023-07-30_Race/'},
#              '08.27': {'https://livetiming.formula1.com/static/2023/2023-08-27_Dutch_Grand_Prix/2023-08-27_Race/'},
#              '09.03': {'https://livetiming.formula1.com/static/2023/2023-09-03_Italian_Grand_Prix/2023-09-03_Race/'},
#              '09.17': {'https://livetiming.formula1.com/static/2023/2023-09-17_Singapore_Grand_Prix/2023-09-17_Race/'},
#              '09.24': {'https://livetiming.formula1.com/static/2023/2023-09-24_Japanese_Grand_Prix/2023-09-24_Race/'},
#              '10.08': {'https://livetiming.formula1.com/static/2023/2023-10-08_Qatar_Grand_Prix/2023-10-08_Race/'},
#              '10.22': {'https://livetiming.formula1.com/static/2023/2023-10-22_United_States_Grand_Prix/2023-10'
#                        '-22_Race/'},
#              '10.29': {'https://livetiming.formula1.com/static/2023/2023-10-29_Mexico_Grand_Prix/2023-10-29_Race/'},
#              '11.05': {'https://livetiming.formula1.com/static/2023/2023-11-05_Brazilian_Grand_Prix/2023-11-05_Race/'},
#              '11.18': {'https://livetiming.formula1.com/static/2023/2023-11-18_Vegas_Grand_Prix/2023-11-18_Race/'},
#              '11.26': {'https://livetiming.formula1.com/static/2023/2023-11-26_Austrian_Grand_Prix/2023-11-26_Race/'}
#              }
#
#
# # Получение текущей даты
# current_date = datetime.datetime.now().strftime('%m.%d')
#
# # Получение ссылки на основе текущей даты
# urls = urls_q_dict.get(current_date)
#
# # Получение первого элемента ссылки и преобразование в текстовый формат
# urls_q_text = str(next(iter(urls)))
#
# print(urls_q_text[52:54])
# print(urls_q_text[85:87])
