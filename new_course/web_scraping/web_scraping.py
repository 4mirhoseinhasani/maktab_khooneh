"""
In this project, you are going to use web scraping technique to extract information from a website. You need to collect information like page title, a specific class, and an image from a web page.

Project Objective:

You need to extract the following information from a website of your choice (for example, an online library or bookstore website):

Web page title
Information inside a specific class (for example, the title of a book or product)
Image link related to the book or product
To do this, you will use the requests and BeautifulSoup libraries.
"""

import requests
import bs4
from tabulate import tabulate

    # request to site
re = requests.get("https://openart.ai/workflows/templates")

    # save data in text format
data = re.text
soup = bs4.BeautifulSoup(data, 'html.parser')

    # get page title in text format
title_tag = soup.select('title')
title = title_tag[0].text

    # find all Topic's in page
elements = soup.find_all(class_='MuiTypography-root MuiTypography-subtitle1 css-5adajd')
element_list = []
for element in elements:
    element_list.append(element.text)

    # find all image's related to Topic's
images = soup.find_all('img')
image_url_list = []
for image in images:
    image_url = image.get('src')
    if image_url.endswith('.webp'):
        image_url_list.append(image_url)

    # all data extracted from the webpage was organized with "tabulate" library 
table_data = list(zip(element_list, image_url_list))
headers = ['Topic', 'img_url']

print(f"page title is: {title}")
print(tabulate(table_data, headers=headers, tablefmt='grid'))
