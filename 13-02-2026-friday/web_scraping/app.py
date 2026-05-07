import requests
from bs4 import BeautifulSoup

web =requests.get("https://www.tutorialsfreak.com/")
print(web)
# print(web.content)

soup = BeautifulSoup(web.content, 'html.parser' )

soup.prettify()

# print(soup.title)
# print(soup.title.name)
# print(soup.p)
# print(soup.a)
print(soup.h1)

tag = soup.html

type(tag)

tag = soup.h1

tag =soup.p