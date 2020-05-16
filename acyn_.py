import timeit
import grequests
from lxml import etree

start = timeit.default_timer()

urls = [
    'https://nomes.club/nomes-populares-brasil/',
    'https://www.passwordrandom.com/most-popular-passwords',
]

rs = (grequests.get(u) for u in urls)

mapa = grequests.map(rs)

x = mapa[0]

y = mapa[1]

tree = etree.HTML(x.text)

lis = tree.xpath('//ol/li//a')

nomes = [li.text for li in lis]

print(nomes)

tree2 = etree.HTML(y.text)

lis2 = tree2.xpath('//tr/td[2]')

senhas = [li.text for li in lis2]

print(senhas)

stop = timeit.default_timer()

print('Time: ', stop - start)  