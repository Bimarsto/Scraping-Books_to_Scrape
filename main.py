import requests
from bs4 import BeautifulSoup
import csv
import os
from categories import get_category_products_information
from constants import main_url, csv_folder


def test_csv_folder():
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

def save_products_information_in_csv(category_name, category_products_information):
    test_csv_folder()
    with open(csv_folder + '/' + category_name + '.csv', 'w',newline='', encoding="utf-8") as file:
        headers = ['product_page_url', 'upc', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available',
                   'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.writer(file)
        writer.writerow(headers)
        for product in category_products_information:
            writer.writerow((product))


response = requests.get(main_url)
if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    for url in soup.find('ul', 'nav-list').findChild('ul').findAll('a'):
        data = get_category_products_information(main_url + '/' + url.get('href'))
        category_products_information = data[1]
        category_name = data[0]
        save_products_information_in_csv(category_name, category_products_information)