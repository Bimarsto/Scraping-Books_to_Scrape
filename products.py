import requests
from bs4 import BeautifulSoup
from constants import main_url


product_page_url = main_url + '/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html'


def convert_star_rating(star_rating):
    if star_rating[1] == 'One':
        review_rating = '1'
    elif star_rating[1] == 'Two':
        review_rating = '2'
    elif star_rating[1] == 'Three':
        review_rating = '3'
    elif star_rating[1] == 'Four':
        review_rating = '4'
    elif star_rating[1] == 'Five':
        review_rating = '5'
    else:
        review_rating = '0'
    return review_rating


def format_data(string_data):
    data = string_data
    while 'â\x80¢' in data:
        data = data.replace('â\x80¢','—')
    while 'Â\xa0' in data:
        data = data.replace('Â\xa0',' ')
    while 'â\x80½' in data:
        data = data.replace('â\x80½', '!?')
    while 'â\x80¨' in data:
        data = data.replace('â\x80¨', '')
    while 'â' in data:
        data = data.replace('â', "'")
    while 'â' in data:
        data = data.replace('â', "'")
    while 'Â£' in data:
        data = data.replace('Â£', '£')
    while 'â\x80\x99' in data:
        data = data.replace('â\x80\x99', "'")
    while 'â\x80\x94' in data:
        data = data.replace('â\x80\x94', '—')
    while 'â' in data:
        data = data.replace('â', '—')
    while 'â' in data:
        data = data.replace('â', '—')
    while 'â' in data:
        data = data.replace('â', '"')
    while 'â' in data:
        data = data.replace('â', '"')
    while 'â¦' in data:
        data = data.replace('â¦', '...')
    return data


def format_number_available(raw_number_available):
    number_available = raw_number_available.replace('In stock (', '')
    number_available = number_available.replace(' available)', '')
    return number_available

def format_category(raw_category):
    category = raw_category.replace('\n','')
    return category


def get_product_information(product_page_url):
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        product_information = soup.find('table', 'table-striped',)
        upc = product_information.find(string='UPC').findParent('tr').findChild('td').text
        price_including_tax = format_data(product_information.find(string='Price (incl. tax)').findParent('tr').findChild('td').text)
        price_excluding_tax = format_data(product_information.find(string='Price (excl. tax)').findParent('tr').findChild('td').text)
        image_url = soup.find('img').attrs['src'].replace('../..', main_url)
        if soup.find(string='Product Description'):
            product_description = format_data(soup.find(string='Product Description').findNext('p').text)
        else:
            product_description = ''
        number_available = format_number_available(product_information.find(string='Availability').findParent('tr').findChild('td').text)
        category = format_category(soup.find('ul', 'breadcrumb').find(string='Books').findNext('li').text)
        title = format_data(soup.find('h1').text)
        star_rating = soup.find('p', 'star-rating').attrs['class']
        review_rating = convert_star_rating(star_rating)
        product_information_data = [product_page_url, upc, title, price_including_tax, price_excluding_tax,
                                    number_available, product_description, category, review_rating, image_url]
        return product_information_data

print(get_product_information(product_page_url))
