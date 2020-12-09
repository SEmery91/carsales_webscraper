import requests
from bs4 import BeautifulSoup

# Find base URL for make and model (To do: add to function with make/ model beinfunction)
class CarInfo:
    def __init__(self, make, model):
        self.make = make
        self.model = model

        # Get base url for make/ model
        base_url = f"https://www.carsales.com.au/cars/{self.make}/{self.model}/?sort=LastUpdated"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        page = requests.get(base_url, headers=headers)

        # Get page content in lxml format
        self.list_page = BeautifulSoup(page.content, 'html.parser')

    def individual_pages(self):
        # Get individual car cards
        cards = self.list_page.find_all(class_="listing-item card standard")
        links = []
        for i in cards:
            header = i.h3
            link_box = i.find(class_='carousel slide lazy js-encode-search')
            link = f"https://www.carsales.com.au/cars/{self.make}/{self.model}" + link_box.get('href')
            links.append(link)
        return links
