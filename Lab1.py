from bs4 import BeautifulSoup # импортируем библиотеку BeautifulS
import requests # импортируем библиотеку requests
import fake_useragent
def parse():
    ua= fake_useragent.UserAgent()
    headers={"User-Agent": ua.random}
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250' # передаем необходимы URL адрес
    page = requests.get(url, headers=headers)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    map = {}
    block = soup.findAll('tr')
    for data in block:
        movie=data.find('td', class_='titleColumn')
        rating=data.find('td', class_='ratingColumn imdbRating')
        if movie is not None and rating is not None:
            mov = " ".join(movie.text.replace('\n', '').split())
            rat = rating.text.replace('\n', '')
            map[mov] = rat

    print(map)
