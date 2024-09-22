import cloudscraper
import requests

from bs4 import BeautifulSoup
from json import loads as load_dictionary

url = ""

scraper = cloudscraper.create_scraper()

html = scraper.get(url).text
soups = BeautifulSoup(html, 'html.parser')

dictionary = load_dictionary(soups.find(id="__NEXT_DATA__").text)

image_names = [f"{name['b2key'][:-5]}-m.jpg" for name in dictionary["props"]["pageProps"]["chapter"]["md_images"]]

for image in image_names:
    with open(image, "wb") as f:
        bytes = requests.get(f"https://meo.comick.pictures/{image}").content
        f.write(bytes)
        print(f"Successfully Extracted: {image}")