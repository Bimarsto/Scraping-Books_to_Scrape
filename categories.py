import requests
from bs4 import BeautifulSoup
import csv
from products import get_product_information
from constants import main_url, products_path

#main_url = 'http://books.toscrape.com'
#categories_path = '/catalogue/category/books'
#products_path = '/catalogue'
#category_page_url = main_url + categories_path + '/add-a-comment_18/index.html'
products_information_data = []


def find_number_of_pages(number_of_products):
    number_of_pages = int(round(number_of_products/20,0))
    return str(number_of_pages)


def format_product_url(product_url):
    product_page_url = main_url + products_path + product_url.replace('../../..','')
    return product_page_url


def get_page_products_information(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'lxml')
    products_in_page = soup.find('ol')
    for product in products_in_page.findAll('h3'):
        product_url = format_product_url(product.find('a')['href'])
        print(product_url)
        products_information_data.append(get_product_information(product_url))
        print('Livre terminé!')


def get_category_products_information(category_page_url):
    response = requests.get(category_page_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        category_name = soup.find('h1').text
        number_of_products = soup.find('form').findNext('strong').text
        if int(number_of_products) < 20:
            number_of_pages = 1
        else:
            number_of_pages = int(soup.find('li', 'current').text.replace(' Page 1 of ','').replace(' ',''))
        #number_of_pages = find_number_of_pages(int(number_of_products))
        print(category_page_url)
        print(category_name +'=> Nombre de pages : ' + str(number_of_pages))
        if number_of_pages == 1 :
            get_page_products_information(category_page_url)
        else:
            for i in range(int(number_of_pages)):
                if i == 0:
                   get_page_products_information(category_page_url)
                else:
                    get_page_products_information(category_page_url.replace('index','page-' + str(i + 1)))
        print('Catégorie ' + category_name + ' terminée!')
        return [category_name, products_information_data]