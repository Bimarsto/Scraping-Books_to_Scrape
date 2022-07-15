import requests
from bs4 import BeautifulSoup
import csv
from categories import get_category_products_information
from constants import main_url

#main_url = 'http://books.toscrape.com'
#categories_path = '/catalogue/category/books'
#category_page_url = main_url + categories_path + '/add-a-comment_18/index.html'


def save_products_information_in_csv(product_information_data):
    with open('products.csv', 'w',newline='', encoding="utf-8") as file:
        headers = ['product_page_url', 'upc', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available',
                   'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.writer(file)
        writer.writerow(headers)
        for product in product_information_data:
            print(product)
            writer.writerow((product))
        #writer.writerows(product_information_data)
    return


response = requests.get(main_url)
if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    all_products_information = []
    for url in soup.find('ul', 'nav-list').findChild('ul').findAll('a'):
        category_products_information = get_category_products_information(main_url + '/' + url.get('href'))
    for product in category_products_information:
        all_products_information.append(product)
    print(all_products_information)
    save_products_information_in_csv(all_products_information)