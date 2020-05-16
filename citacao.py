import timeit
import grequests
from lxml import etree

start = timeit.default_timer()

urls = ['http://frasedodia.net/']

rs = (grequests.get(u) for u in urls)

mapa = grequests.map(rs)

tree = etree.HTML(mapa[0].text)

frase = tree.xpath('//div[2]/div/div/div[4]/div/div/div[1]/div/div[1]/a')[0]

autor = tree.xpath('//div[2]/div/div/div[4]/div/div/div[1]/div/h5/a')[0]

print(frase.text, '\n', autor.text)

stop = timeit.default_timer()

print('Time: ', stop - start)
