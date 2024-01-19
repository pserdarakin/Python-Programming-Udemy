import requests

from bs4 import BeautifulSoup


url = 'https://www.yemeksepeti.com/izmir'
response = requests.get(url)

html_iceriği = response.content

soup = BeautifulSoup(html_iceriği,'html.parser')

print(soup.find_all('div',{'class':'row'}))
