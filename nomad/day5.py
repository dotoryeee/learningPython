import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

def getHTML():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return(soup)

def extractTable(soup):
    tableData = soup.find('table',{'class':'table'}).find_all('td')
    table = []
    for i in tableData:
        table.append(i.string)
    return(table)

def makeList(table):
    datas = []
    num = 0
    for data in table:
        if num == 0 or num % 4 == 0:
            country = {}
            country['name'] = data
            country['code'] = table[num+2]
            datas.append(country)
        num += 1
    return(datas)

def printList(list):
    num = 0
    for i in list:
        print(f'# {num} {i["name"]}')
        num += 1

def selectNumber(len):
    print('choose number from the list')
    while True:
        select = int(input('# :'))
        if select >= 0 and select <= len:
            return select
def main():
    html = getHTML()
    table = extractTable(html)
    list = makeList(table)
    printList(list)
    while True:
        select = selectNumber(len(list))
        print(f'code is {list[select]["code"]}')

main()