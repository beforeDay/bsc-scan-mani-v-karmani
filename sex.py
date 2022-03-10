import cloudscraper
from bs4 import BeautifulSoup
import time

sexik = 1
url = 'https://bscscan.com/address/Кошель сюда'
sex = cloudscraper.create_scraper()
while True:
    
    time.sleep(5)
    response = sex.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    f = open('Res.txt', 'w')
    f.close()
    items2 = soup.find_all('div', class_='col-md-8',)
    for quote in items2:
        aaaa=f'{quote.text}'
        s = open("Res.txt", "a").write(f'{aaaa}')
    with open('Res.txt') as f:
        i = 1
        for line in f:
            if i == (int(sexik)):
                x,y = line.split("BNB", 1)
                g,h = y.split("(", 1)
                break
            i += 1
    print('Balance: ', g)
