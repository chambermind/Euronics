from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

page_url = "https://www.euronics.lv/products-en/s/525/computers-and-tablets/tablets"
uClient = uReq(page_url)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()
containers = page_soup.find("ul", {"class": "oi-list oi-grid-products"}).findAll("li", {"class": "oi-item"})

filename = "Euronics.csv"
f = open(filename, "w")

headers = "Product name, Product ID, Product price \n"
f.write(headers)
for container in containers:
    title_container = container.find("h3", {"class": "name"}).text
    product_name = container.find("h3", {"class": "name"}).text
    productID = container.find("p", {"class": "productID"}).text
    price = container.find("p", {"class": "price"}).text
    # print(price_discount)

print("product_name: " + product_name + "\n")
# noinspection PyUnboundLocalVariable
print("productID: " + productID + "\n")
print("price: " + price + "\n")

with open("Euronics.csv", 'w') as f:

    for header in headers:
        f.write(product_name + "," + productID + "," + price + "\n")

f.close()
# print(brand)
