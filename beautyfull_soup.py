import requests
from BeautifulSoup import BeautifulSoup
import sys
 
url = 'http://en.wikipedia.org/wiki/Python'
response = requests.get(url)
html = response.content
soup = BeautifulSoup (html)
 
print(soup.prettify())