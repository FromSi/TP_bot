import requests
from bs4 import BeautifulSoup


def get_weather(link):
    """Получение погоды на сегодня по ссылке www.gismeteo.com.
    
    Аргументы Функции:
    link -- ссылка на www.gismeteo.com с отсылкой на город
    """
    return _handler_weather(link)


def _get_html(link):
    """Получить HTML сайта www.gismeteo.com.
    
    Аргументы Функции:
    link -- ссылка на www.gismeteo.com с отсылкой на город
    """
    response = requests.get(link, headers={"User-Agent": "Firefox/67.0.4"})

    return response.text


def _handler_weather(link):
    """Обработчик сайта www.gismeteo.com.
    
    Аргументы Функции:
    link -- ссылка на www.gismeteo.com с отсылкой на город
    """
    soup = BeautifulSoup(_get_html(link), 'lxml')
    divs = soup.find(
                    'div', 
                    {'class': 'forecast_frame hw_wrap'}
                ).find(
                    'div', 
                    {'class': 'widget__wrap'}
                ).find(
                    'div', 
                    {'class': 'widget__container'}
                )
    
    return _get_data(divs)
    

def _get_data(divs):
    """Получить готовые данные.
    
    Аргументы Функции:
    divs -- объект с контентом погоды (новая точка ROOT)
    """
    times = _get_times(divs)
    temps = _get_temps(divs)
    winds = _get_winds(divs)

    data = [
        [
            times[2].find('span').text,
            temps[2].find('span').text,
            winds[2].find('span').text.replace("\n", "").replace(" ", "")
        ],
        [
            times[3].find('span').text,
            temps[3].find('span').text,
            winds[3].find('span').text.replace("\n", "").replace(" ", "")
        ],
        [
            times[4].find('span').text,
            temps[4].find('span').text,
            winds[4].find('span').text.replace("\n", "").replace(" ", "")
        ],
        [
            times[5].find('span').text,
            temps[5].find('span').text,
            winds[5].find('span').text.replace("\n", "").replace(" ", "")
        ],
        [
            times[6].find('span').text,
            temps[6].find('span').text,
            winds[6].find('span').text.replace("\n", "").replace(" ", "")
        ],
        [
            times[7].find('span').text,
            temps[7].find('span').text,
            winds[7].find('span').text.replace("\n", "").replace(" ", "")
        ],
    ]

    return data


def _get_times(divs):
    """Получить время температур.
    
    Аргументы Функции:
    divs -- объект с контентом погоды (новая точка ROOT)
    """
    return divs.find(
                    'div', 
                    {'class': 'widget__row widget__row_time'}
                ).findAll(
                    'div', 
                    {'class': 'widget__item'}
                )


def _get_temps(divs):
    """Получить объект с температурами.
    
    Аргументы Функции:
    divs -- объект с контентом погоды (новая точка ROOT)
    """
    return divs.find(
                    'div', 
                    {'class': 'widget__row widget__row_table widget__row_temperature'}
                ).find(
                    'div', 
                    {'class': 'values'}
                ).findAll(
                    'div', 
                    {'class': 'value'}
                )


def _get_winds(divs):
    """Получить объект с ветрами.
    
    Аргументы Функции:
    divs -- объект с контентом погоды (новая точка ROOT)
    """
    return divs.find(
                    'div', 
                    {'class': 'widget__row widget__row_table widget__row_wind-or-gust'}
                ).findAll(
                    'div', 
                    {'class': 'widget__item'}
                )