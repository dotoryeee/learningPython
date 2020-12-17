import requests
import os

def connect(url):
  r = requests.get(url)
  if r.status_code == 200:
    print(f'{url} is UP')
  else:
    print(f'{url} is DOWN')

def main():
  while True:
    os.system('clear')
    print('write URL or URLs you want to check(seperate by comma)')
    urls = input('')
    urls = urls.split(',')
    for url in urls:
      url = url.strip()
      if url.count('.') == 0:
        print(f'{url} is invaild URL')
      elif url.count('http') == 0:
        url = 'http://' + url
        connect(url)
      else:
        connect(url)
    select = input('retry? y/n : ')
    if select.upper() == 'N':
      print('program exit')
      return

main()