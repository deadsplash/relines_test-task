from bs4 import BeautifulSoup
import requests
import textwrap
from flask import Flask, render_template, redirect

app = Flask(__name__)


def parser(url, save_img=True, save_to_txt=True, line_length=50):

    save = dict()
    r = str()

    try:
        r = requests.get(url).text
    except Exception as ex:
        print('Requests error:  ', ex)
        exit()

    soup = BeautifulSoup(r, 'lxml')

    find_all_articles = soup.findAll('article')
    finder = 'span'

    if len(find_all_articles) < 2:
        return print('Unable to parse this URL')

    if len(find_all_articles[1].find(finder).text.strip()) < 30:
        finder = 'h2'
    else:
        print(len(find_all_articles))
        pass

    #   used for article type HTML
    for i in range(len(find_all_articles)):

        try:

            # ищем названия статей по странице
            item = find_all_articles[i].find(finder).text
            print(item)
            save[item] = ""

            if save_img is True and len(item) > 5:
                try:
                    # чистим ссылку от всего лишнего
                    pic = str(find_all_articles[i].find('img').get('src')).replace('//', '').replace('https:', '')
                    print(pic + '\n' + '\n')
                    # делаем человеческие отступы
                    save[item] = pic + '\n'
                except Exception:
                    pass

        except Exception:
            pass

    if save_to_txt is True:
        with open('result.txt', 'w', encoding='UTF-8') as f:
            for i in save:
                article_list = textwrap.wrap(i, line_length)
                for article in article_list:
                    f.write(article + '\n')
                f.write(save[i] + '\n')


@app.route('/', methods=['GET'])
def parser():
    return 'Hello'


def main():

    print("URL: ")
    url = str(input())

    print('Do you want to collect IMG links? Y/N')
    checker = str(input()).upper()
    if checker == 'Y':
        save_img = True
    elif checker == 'N':
        save_img = False
    else:
        save_img = False
        print('Wrong input, script will not collect IMG links.')

    print('Do you want to save your data into TXT file? Y/N')
    checker = str(input()).upper()
    if checker == 'Y':
        save_to_txt = True
    elif checker == 'N':
        save_to_txt = False
    else:
        save_to_txt = False
        print('Wrong input, script will not save into text.')

    print('Please, define line length: ')
    line_length = int()
    try:
        line_length = int(input())
    except Exception as ex:
        print('Error: ', ex)
        exit()

    parser(url, save_img=save_img, save_to_txt=save_to_txt, line_length=line_length)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
