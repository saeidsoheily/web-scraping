__author__ = 'Saeid SOHILY-KHAH'
"""
Web scraping algorithms: Web scraping using Beautiful Soup and Requests (ebay website)
To run in terminal: $ python3  requests_webscraping_ebay  <https://www.ebay.fr/...> 
"""
import re
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

pd.set_option('display.expand_frame_repr', False)  # extend the output display


# Extract float number from a string
def extract_number(text):
    text = text.replace(',', '.')
    num = re.findall(r"[-+]?\d*\.\d+|\d+", text)
    try:
        number = float(num[-1])
    except:
        number = 0
    return number


# ------------------------------------------------ MAIN ----------------------------------------------------
if __name__ == '__main__':
    # Set (ebay) url to scrap
    if len(sys.argv) > 1:
        ebay_url = str(sys.argv[-1])   # as a python command line argument
    else:
        ebay_url = "https://www.ebay.fr/sch/i.html?_nkw=iphone"  # default

    # Check status code for a valid url
    try:
        request = requests.get(ebay_url)
        status_code = request.status_code
    except:
        status_code = -1

    if status_code != 200:
        sys.exit("Requested url is not valid or cannot be found!")

    # Pulling data out of HTML (or XML) files
    data = request.text
    soup = BeautifulSoup(data, "lxml")

    # Navigate data structure (limit the search)
    objects = soup.find_all('li', attrs={'class': 's-item'}) # get all items inside li tag (ebay HTML)

    # Scrap objects in data
    names = []
    prices = []
    locations = []
    shippings = []
    for object in objects:
        object_name = " "
        object_price = " "
        object_location = " "
        object_shipping = " "
        for name in object.find_all('h3', attrs={'class': "s-item__title"}): # title attribute in ebay
            if (str(name.find(text=True, recursive=False)) != "None"):
                object_name = str(name.find(text=True, recursive=False))
                names.append(object_name)

        # Scrap price, location and shipping values for named objects
        if (object_name != " "):
            price = object.find('span', attrs={'class': "s-item__price"}) # price attribute in ebay
            if price != None:
                if price.find('span', attrs={'class': "ITALIC"}): # price (possible) attribute in ebay
                    price = price.find('span', attrs={'class': "ITALIC"})
                object_price = str(price.find(text=True, recursive=False))
            else:
                object_price = " "
            prices.append(object_price)

            location = object.find('span', attrs={'class': "s-item__location s-item__itemLocation"}) # location attribute in ebay
            if location != None:
                object_location = str(location.find(text=True, recursive=False))
            else:
                object_location = " "
            locations.append(object_location)

            shipping = object.find('span', attrs={'class': "s-item__shipping s-item__logisticsCost"}) # shipping attribute in ebay
            if shipping != None:
                if shipping.find('span', attrs={'class': "ITALIC"}): # shipping (posible) attribute in ebay
                    shipping = shipping.find('span', attrs={'class': "ITALIC"})
                object_shipping = str(shipping.find(text=True, recursive=False))
            else:
                object_shipping = " "
            shippings.append(object_shipping)

    df = pd.DataFrame({"name": names, "price": prices, "location": locations, "shipping": shippings})
    df['total_price'] = df.apply(lambda x: extract_number(x['price']) + extract_number(x['shipping']), axis=1)
    print(df.head())