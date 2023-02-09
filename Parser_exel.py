from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import Parser
import pandas as pd


def parse():
    url = 'https://www.chitai-gorod.ru/search?q=Python' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html1.parser") # передаем страницу в bs4
    block = soup.findAll('section', class_='products-list') # находим  контейнер с нужным классом
    file_parser = open("file_parser1.txt", "w+")
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('div', class_='product-price__value product-price__value--discount'): # находим тег <a>
            file_parser.write(data.text)
    file_parser.close()


if __name__ == '__main__':
    Parser.parse()