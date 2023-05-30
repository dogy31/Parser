from card import Cardcod

import requests
from bs4 import BeautifulSoup

# Определяем заголовки для запроса
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Отправляем GET-запрос на страницу с погодой для Москвы с заголовками
url = 'https://world-weather.ru/pogoda/russia/barnaul/'
response = requests.get(url, headers=headers)

# Извлекаем текущую температуру из HTML-кода страницы
soup = BeautifulSoup(response.content, 'html.parser')

# Найти все элементы с классом "div"
elements = soup.find_all('div', class_='day-week')

first_day = elements[0]
second_day = elements[1]
third_day = elements[2]

elements = soup.find_all('div', class_='numbers-month')

first_numbers = elements[0]
second_numbers = elements[1]
third_numbers = elements[2]

elements = soup.find_all('div', class_='month')

first_month = elements[0]
second_month = elements[1]
third_month = elements[2]

elements = soup.find_all('div', class_='day-temperature')

first_temperature = elements[0]
second_temperature = elements[1]
third_temperature = elements[2]

elements = soup.find_all('div', class_='night-temperature')

first_night_temperature = elements[0]
second_night_temperature = elements[1]
third_night_temperature = elements[2]

first_data = first_numbers.text + " " +  first_month.text
second_data = second_numbers.text + " " +  second_month.text
third_data = third_numbers.text + " " +  third_month.text

first_temperature = "Днём: " + first_temperature.text
second_temperature = "Днём: " + second_temperature.text
third_temperature = "Днём: " + third_temperature.text

first_night_temperature = "Ночью: " + first_night_temperature.text
second_night_temperature = "Ночью: " + second_night_temperature.text
third_night_temperature = "Ночью: " + third_night_temperature.text

Cardcod(first_day, first_data, first_temperature, second_day, second_data ,second_temperature, 
        third_day , third_data, third_temperature,first_night_temperature,second_night_temperature,third_night_temperature )