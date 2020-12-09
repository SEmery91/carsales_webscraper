import scraper

def main():
    car_info = scraper.CarInfo('mitusbishi', 'outlander')
    car_page = car_info.individual_pages()
    print(car_page)


if __name__ == main():
    main()

