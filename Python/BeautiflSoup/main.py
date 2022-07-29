import re
import requests
from bs4 import BeautifulSoup
import re
# response = requests.get('https://news.ycombinator.com/')
# data = response.text
# soup = BeautifulSoup(data,'html.parser')
# titl = soup.find_all(class_='titlelink')
# article_text = []
# article_link = []
# article_score = []
# for strings in titl:
#     article_text.append(strings.getText('a'))
#     article_link.append(strings.get('href'))

# score = soup.find_all(class_='score')
# for scores in score:
#     itm = scores.getText('span')
#     article_score.append(int(itm.split(' ')[0]))


# indx = article_score.index(max(article_score))

# print(article_text[indx],article_link[indx])

url = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
dat = soup.find_all(name='h3',class_='jsx-4245974604')
print(dat)