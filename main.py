from bs4 import BeautifulSoup
import requests


url = 'https://xakep.ru/'


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
    finder = 'span'

    if len(find_all_articles) < 2:
        print('Unable to parse this URL')
        exit()

    if len(find_all_articles[1].find(finder).text) < 30:
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
                except:
                    pass

        except Exception:
            pass

    if save_to_txt is True:
        with open('result.txt', 'w', encoding='UTF-8') as f:
            for i in save:
                f.write(i + '\n' + save[i] + '\n')


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

    parser(url, save_img=save_img, save_to_txt=save_to_txt)


if __name__ == '__main__':
    main()
