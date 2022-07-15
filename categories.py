import requests
from bs4 import BeautifulSoup
import csv
from products import get_product_information

main_url = 'http://books.toscrape.com'
categories_path = '/catalogue/category/books'
products_path = '/catalogue'
category_page_url = main_url + categories_path + '/add-a-comment_18/index.html'


def find_number_of_pages(number_of_products):
    if number_of_products - round(number_of_products/20, 0) >= 0.5:
        number_of_pages = int(round(number_of_products/20,0) + 1)
    else:
        number_of_pages = int(round(number_of_products/20,0))
    return str(number_of_pages)


def format_product_url(product_url):
    product_page_url = main_url + products_path + product_url.replace('../../..','')
    return product_page_url


def save_products_information_in_csv(product_information_data):
    with open('products.csv', 'w' ,newline='') as file:
        headers = ['product_page_url', 'upc', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available',
                   'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(product_information_data)
    return


response = requests.get(category_page_url)
if response.ok:
    products_information_data = []
    soup = BeautifulSoup(response.text, 'lxml')
    number_of_products = soup.find('form').findNext('strong').text
    number_of_pages = find_number_of_pages(int(number_of_products))
    for i in range(int(number_of_pages)):
        if i == 0:
            products_in_page = soup.find('ol')
            for product in products_in_page.findAll('h3'):
                product_url = format_product_url(product.find('a')['href'])
                products_information_data.append(get_product_information(product_url))
        else:
            response = requests.get(category_page_url.replace('index','page-' + str(i + 1)))
            soup = BeautifulSoup(response.text, 'lxml')
            products_in_page = soup.find('ol')
            for product in products_in_page.findAll('h3'):
                product_url = format_product_url(product.find('a')['href'])
                products_information_data.append(get_product_information(product_url))
        print('Page ' + str(i + 1) + ' OK!')
    save_products_information_in_csv(products_information_data)
