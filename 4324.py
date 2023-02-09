from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests
import pandas as pd

top_films = {
    'Name': '',
    'Rating': ''
}
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'  # передаем необходимы URL адрес
page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
print(page.status_code)  # смотрим ответ
soup = BeautifulSoup(page.text, "html.parser")
base = soup.findAll('td', class_="titleColumn")

for name in base:
    top_films['Name'] = str(name.find('a').text)
    print(name.find('a').text)

base = soup.findAll('td', class_="ratingColumn imdbRating")

for rating in base:
    print(rating.find('strong').text)

print(top_films)