from bs4 import BeautifulSoup
import requests


url = 'https://habr.com/ru/'

#print(soup.find('main').text.strip())

#   habr и howtogeek держат главное в h2
# find_all_articles = soup.find('main').findAll('h2') # howtogeek.com personally
# find_all_articles = soup.findAll('h2') # работает с обоими

# find_all_articles = soup.find('div').findAll('a')  # hacker.ru

# find_all_articles = soup.find('div').findAll('span')  # https://dtf.ru/

# print(find_all_articles)   # for debug needs


def parser(url, save_img=False, save_to_txt=False):

    save = dict()
    r = str()

    try:
        r = requests.get(url).text
    except Exception as ex:
        print('Error:  ', ex)
        exit()

    soup = BeautifulSoup(r, 'lxml')

    find_all_articles = soup.findAll('article')

    #   used for article type HTML
    for i in range(len(find_all_articles)):

        try:

            item = find_all_articles[i].find('h2').text
            print(item)
            save[item] = ""

            if save_img is True and len(item) > 5:
                try:
                    pic = str(find_all_articles[i].find('img').get('src')).replace('//', '').replace('https:', '')
                    print(pic + '\n' + '\n')
                    save[item] = pic + '\n'
                except:
                    pass
        except:
            pass

    if save_to_txt is True:
        with open('result.txt', 'w', encoding='UTF-8') as f:
            for i in save:
                f.write(i + '\n' + save[i] + '\n')


parser(url, save_img=False, save_to_txt=True)