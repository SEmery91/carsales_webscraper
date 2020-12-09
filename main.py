import requests
from bs4 import BeautifulSoup

make = "Mitsubishi"
model = "Outlander"

base_url = f"https://www.carsales.com.au/cars/{make}/{model}/?sort=LastUpdated"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
page = requests.get(base_url, headers=headers)

soup = BeautifulSoup(page.content, 'lxml')

topspot = soup.find_all(class_="listing-item card standard")
links = soup.find_all(class_="listing-item card showcase")
links.append(topspot)

car = links[0].find(class_='carousel slide lazy js-encode-search')
car_link = car.get('data-href')
print(car_link)

car_page = requests.get()

# print(links)

# for link in links:
#     print(link)
#     # title = link.find('data-webm-clickvalue')
#     make = link.get('data-webm-make')
#     model = link.get('data-webm-model')
#     price = link.get('data-webm-price')
#     id = link.get('id')
#     # print(title)
#     print(make)
#     print(model)
#     print(price)
#     print(id)