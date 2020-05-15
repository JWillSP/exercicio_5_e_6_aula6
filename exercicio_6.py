from time import sleep
from collections import defaultdict
from selenium.webdriver import Firefox


nome = ['Will', 'Paulo', 'Fábio', 'Pedro', 'Tiago']

default_nome = defaultdict(lambda: iter(nome))

nav = Firefox()

nav.get('https://selenium.dunossauro.live/exercicio_06.html')

sleep(2)

while True:

    target_txt = nav.find_element_by_css_selector('header span').text

    if target_txt == '... Mentira, você conseguiu terminar':

        break

    n = next(default_nome[target_txt])

    print(target_txt, ' ', n)

    t = nav.find_element_by_css_selector(f'.form-{target_txt} [type=text]')

    t.send_keys(n)

    s = nav.find_element_by_css_selector(f'.form-{target_txt} [type=password]')

    s.send_keys('45678')

    e = nav.find_element_by_css_selector(f'.form-{target_txt} [type=submit]')

    e.click()

    sleep(3)

nav.close()
