from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import Parser


def parse():
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div', id='pagecontent') # находим  контейнер с нужным классом
    file_parser = open("file_parser.txt", "w+")
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('a'): # находим тег <a>
            file_parser.write(data.text)
    file_parser.close()


if __name__ == '__main__':
    Parser.parse()