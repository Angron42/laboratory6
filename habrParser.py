from bs4 import BeautifulSoup
import requests

def countWords(string, words = {}):
    for word in string.split(' '):
        if not word in words:
            words[word] = 1
            continue

        words[word] += 1
    
    return words

request = requests.get('https://habr.com/ru/company/talenttech/blog/591915/')

if not request.ok:
    print('Ошибка запроса:', request.status_code)
else:
    page = BeautifulSoup(request.text, 'html.parser')
    paragraphs = page.select('#post-content-body > div p')
    words = {}
    for string in paragraphs:
        words = countWords(string.get_text(), words)
    
    aEls = page.select('a')
    imgEls = page.select('img')

    print('Частота появления слов', words)
    print('Частота появления параграфов', len(paragraphs))
    print('Количество ссылок', len(aEls))
    print('Количество изображений', len(imgEls))
