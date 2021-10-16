from bs4 import BeautifulSoup
import requests

'''
1. сначала разбираеся как собрать важные данные со страницы, находим обобщенные параметры поиска
2. добавляем сбор ссылок
3. пишем правильный вывод с переносом строк
3. собираем скрипт в функцию с задаваемыми параметрами
'''


url = 'https://habr.com/ru/'

r = requests.get(url).text

soup = BeautifulSoup(r, 'lxml')

#print(soup.find('main').text.strip())

#   habr и howtogeek держат главное в h2
# find_all_articles = soup.find('main').findAll('span')  # habr.com/ru personally
# find_all_articles = soup.find('main').findAll('h2') # howtogeek.com personally
# find_all_articles = soup.findAll('h2') # работает с обоими

# find_all_articles = soup.find('div').findAll('a')  # hacker.ru

# find_all_articles = soup.find('div').findAll('span')  # https://dtf.ru/

find_all_articles = soup.findAll('article')

# print(find_all_articles)   # for debug needs


for i in range(len(find_all_articles)):
    print("""
        """)
    item = find_all_articles[i].find('h2').text
    print(item)
    try:
        pic = find_all_articles[i].find('img').get('src')
        print(str(pic).replace('//', '').replace('https:', ''))
    except Exception as ex:
        print('no picture here')
        pass

