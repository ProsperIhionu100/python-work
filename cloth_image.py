from bs4 import BeautifulSoup
import requests

BASE = "https://micheal-lyon.github.io/e-commerce-front-end"
page = requests.get('https://micheal-lyon.github.io/e-commerce-front-end/')
soup = BeautifulSoup(page.content,'html.parser')

shirt = soup.select('div.pro img')
descr = soup.select('div.des h5')
price = soup.select('div.star h4')

for i in range(2):
    des = descr [i].text
    price = price[i].text
    
    im = shirt[i].attrs['src']
    
    im =im[1:]
    print(im)
    imagee = requests.get(BASE + im).content     
    
    with open(f'images/{des}-{price} {i}.jpg','wb') as file:
        file.write(imagee)