import requests
from bs4 import BeautifulSoup

main_url = 'http://books.toscrape.com'
product_page_url = main_url + '/catalogue/sharp-objects_997/index.html'

response = requests.get(product_page_url)


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
    if 'â' in data:
        data = data.replace('â', "'")
    elif 'Â£' in data:
        data = data.replace('Â£', '£')
    elif 'â\x80\x94' in data:
        data = data.replace('â\x80\x94', '—')
    return data


def format_number_available(raw_number_available):
    number_available = raw_number_available.replace('In stock (', '')
    number_available = number_available.replace(' available)', '')
    return number_available


def save_product_information_in_csv(product_information_data):
    with open('product.csv', 'w') as file:
        file.write("URL du produit,Code UPC,Titre,Prix TTC,Prix HT,Stock,Desctiption,Catégorie,Note,URL de l'image\n")
        file.write(product_information_data[0] + ',' + product_information_data[1] + ',' + product_information_data[2] +
                    ',' + product_information_data[3] + ',' + product_information_data[4] + ',' +
                    product_information_data[5]  + ',' + product_information_data[7] +
                    ',' + product_information_data[8] + ',' + product_information_data[9] + '\n')


if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    product_information = soup.find('table', 'table-striped',)
    upc = product_information.find(string='UPC').findParent('tr').findChild('td').text
    price_including_tax = format_data(product_information.find(string='Price (incl. tax)').findParent('tr').findChild('td').text)
    price_excluding_tax = format_data(product_information.find(string='Price (excl. tax)').findParent('tr').findChild('td').text)
    image_url = soup.find('img').attrs['src'].replace('../..', main_url)
    # A revoir
    #product_description = format_data(soup.find(string='Product Description').findNext('p').text)
    #
    number_available = format_number_available(product_information.find(string='Availability').findParent('tr').findChild('td').text)
    category = soup.find('ul', 'breadcrumb').find(string='Books').findNext('li').text
    title = soup.find('h1').text
    star_rating = soup.find('p', 'star-rating').attrs['class']
    review_rating = convert_star_rating(star_rating)
    product_information_data = [product_page_url, upc, title, price_including_tax, price_excluding_tax,
                                number_available, product_description, category, review_rating, image_url]
    print(product_information_data)
    save_product_information_in_csv(product_information_data)


