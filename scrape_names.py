import requests
from lxml import etree

x = requests.get('https://nomes.club/nomes-populares-brasil/')

tree = etree.HTML(x.text)

lis = tree.xpath('//ol/li//a')

nomes = [li.text for li in lis]

print(nomes)

y = requests.get('https://www.passwordrandom.com/most-popular-passwords')

tree2 = etree.HTML(y.text)

lis2 = tree2.xpath('//tr/td[2]')

senhas = [li.text for li in lis2]

print(senhas)
