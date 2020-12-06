import requests
from bs4 import BeautifulSoup

print()
result = requests.get('https://kr.indeed.com/jobs?q=%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C&l=')
soup = BeautifulSoup(result.text, 'html.parser')

pagination = soup.find('div',{'class' : 'pagination'})
links = pagination.find_all('a')
pages = []

for  link in links:
    pages.append(link.find('span').string)

print(pages[:-1])