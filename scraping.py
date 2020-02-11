from bs4 import BeautifulSoup
import requests


def run():
    URL = 'https://www.platzi.com/'

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'lxml')
    print(soup.prettify())


if __name__ == '__main__':
    run()
