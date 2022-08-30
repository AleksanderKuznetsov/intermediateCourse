"""
Парсинг сайтов. OLX - автомобили
"""
import time
import json
from bs4 import BeautifulSoup
import requests


def parsing(url):
    """
    Спарсить сайт по ссылке и сложить в json.
    :param url: ссылка на раздел сайта.
    :return: словарь с результатом парсинга.
    """
    # Получить количество страниц.
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html5lib")
    pages = int(soup.find_all('li', {'data-testid': 'pagination-list-item'})[-1].text)
    result = {}

    # Пройти по всем найденным страницам:
    for page in range(1, pages+1):
        response = requests.get(f'https://www.olx.ua/d/transport/legkovye-avtomobili/lug/?currency=USD&page={str(page)}')
        # Если страница не работает
        if response.status_code < 200 or response.status_code > 299:
            return 'Page Error'
        # Спарсить страницу
        soup = BeautifulSoup(response.text, "html5lib")
        # Получить все блоки объявлений.
        ads = soup.find_all('a', {'class': 'css-1bbgabe'})

        # Пройти по всем блокам объявлений на странице.
        for i, ad in enumerate(ads):
            h6 = ad.find('h6', class_='css-v3vynn-Text eu5v0x0').text
            location_date = ad.find_all('p', {'data-testid': 'location-date'})[0].text
            price = ad.find('p', class_='css-wpfvmn-Text eu5v0x0').string
            age_mileage = ad.find('p', class_='css-efx9z5').text
            url = "https://www.olx.ua" + ad.attrs['href']
            # Получить фото. Может не быть в объявлении.
            try:
                photo = ad.find('div', class_='css-gl6djm').find('img').attrs['srcset']
            except KeyError:
                photo = '-'

            # Наполнить словарь результата.
            result[str(page)+"-"+str(i)] = {'title': h6, 'location_date': location_date,
                                            'price': price, 'age_mileage': age_mileage,
                                            'url': url, 'photo': photo}
        # Между страницами сделать паузу.
        time.sleep(2)

    # Сохранить результат в файл
    with open("parsing.json", "w", encoding='utf8') as json_file:
        json.dump(result, json_file)

    return result


# print(parsing('https://www.olx.ua/d/transport/legkovye-avtomobili/lug/?currency=USD'))
