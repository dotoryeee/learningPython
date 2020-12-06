import requests
from bs4 import BeautifulSoup

print()
result = requests.get('https://kr.indeed.com/jobs?q=%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C&l=')
soup = BeautifulSoup(result.text, 'html.parser')

pagination = soup.find('div',{'class' : 'pagination'})
pages = pagination.find_all('a')
spans = []

for  page in pages:
    spans.append(page.find('span'))

for i in range(0, len(spans)-1):
    print(spans[i])
print()

print(spans[:-1])