from selenium.webdriver import Firefox
from time import sleep

nav = Firefox()

nav.get('https://selenium.dunossauro.live/exercicio_05.html')

sleep(2)

for i in range(4):

    target_txt = nav.find_element_by_css_selector('header span').text

    t = nav.find_element_by_css_selector(f'.form-{target_txt} [type=text]')

    t.send_keys('Will')

    s = nav.find_element_by_css_selector(f'.form-{target_txt} [type=password]')

    s.send_keys('45678')

    e = nav.find_element_by_css_selector(f'.form-{target_txt} [type=submit]')

    e.click()

    sleep(2)

nav.close()
