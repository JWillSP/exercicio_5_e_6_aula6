from selenium.webdriver import Firefox
from collections import defaultdict
from time import sleep


nome = ['Will', 'Paulo', 'Fábio', 'Pedro', 'Tiago']

default_nome = defaultdict(lambda: iter(nome))


def get_name(key):
    return next(default_nome[key])


nav = Firefox()

nav.get('https://selenium.dunossauro.live/exercicio_06.html')

sleep(2)

while True:

    target_txt = nav.find_element_by_css_selector('header span').text

    if target_txt == '... Mentira, você conseguiu terminar':

        break

    t = nav.find_element_by_css_selector(f'.form-{target_txt} [type=text]')

    n = get_name(target_txt)

    print(target_txt, ' ', n)

    t.send_keys(n)

    s = nav.find_element_by_css_selector(f'.form-{target_txt} [type=password]')

    s.send_keys('45678')

    e = nav.find_element_by_css_selector(f'.form-{target_txt} [type=submit]')

    e.click()

    sleep(3)

nav.close()
