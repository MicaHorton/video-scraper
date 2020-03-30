import requests
from bs4 import BeautifulSoup

#Set Headers To Seem Legitimate
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})


URL = 'https://ww3.fmovie.sc/free/you-season-1/watching.html/?episode=10565'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
tag = soup.find(id='iframe-embed').get('src')
print(tag)

'''
Doesn't work. 'Src' shows up empty for some reason, probably some Javascript load error or website blocking us?

tag = soup.find(id='iframe-embed')
print(tag.prettify())
print(tag['src'])
'''


