import re
import requests
from lxml import etree
from selenium.webdriver import Firefox


x = requests.get('https://nomes.club/nomes-populares-brasil/')

print(x.text)

# nav = Firefox()

# nav.get('https://nomes.club/nomes-populares-brasil/')

# olista = nav.find_element_by_xpath('//article//ol')

# nomes = re.findall(r'\w+:', olista.text)

# print(nomes)

# nav.close()