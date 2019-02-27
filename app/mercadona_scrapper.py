from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from conf.credentials import password, username
import time
import random


class MercadonaScrapper(object):

    login_url = 'https://www.telecompra.mercadona.es/ns/entrada.php?js=1'
    login_credentials = {
        'username': username,
        'password': password
    }
    login_submit_button = '//input[@type="submit"]'

    search_url = 'https://www.telecompra.mercadona.es/lista.php?busc_ref=%s&posicion_actual=%s'

    def __init__(self):
        self.driver = webdriver.Chrome('bin/chromedriver')
        self.driver.implicitly_wait(2)
        self.login()

    def login(self):
        self.driver.get(self.login_url)

        for key, val in self.login_credentials.items():
            self.driver.find_element_by_id(key).send_keys(val)

        self.driver.find_element_by_xpath(self.login_submit_button).click()

    def get_products(self):
        self.elements = []

        self.search_in_products('a')
        self._scrap_elements()

        return self.elements

    def search_in_products(self, term):
        self.term = term
        self.item = 0
        self.driver.get(self.search_url % (self.term, self.item))

    def _scrap_elements(self):
        prev_len = len(self.elements)
        self.elements = [*self.elements, *self._parse_elements()]
        while prev_len != len(self.elements):
            prev_len = len(self.elements)

            self.next_page()
            self.reload_on_ban()
            self.elements = [*self.elements, *self._parse_elements()]

    
    def next_page(self):
        self.item = self.item + 20
        self.driver.get(self.search_url % (self.term, self.item))
    
    def reload_on_ban(self):
        if 'The requested URL was rejected.' in self.driver.find_element_by_tag_name('body').text:
            url = self.driver.current_url
            self.login()
            self.driver.get(url)

    def _parse_elements(self):
        elements = []
        for tr in self.find_css_elements('tr:not(.tablacabecera)'):
            title, link, price, *_ = tr.find_elements_by_tag_name('td')
            elements.append(
                Product(
                    title.text,
                    float(
                        price.find_element_by_tag_name('span').text
                        .replace(',', '.').split(' ')[0]
                    ),
                    link.find_element_by_tag_name('a').get_attribute(
                        'href') if link.text.strip() else None
                )
            )
        return elements

    def find_css_elements(self, css):
        try:
            return self.driver.find_elements_by_css_selector(css)
        except NoSuchElementException:
            return []

    def find_css_element(self, css):
        elements = self.find_css_elements(css)
        return elements[0] if elements else None

    def __del__(self):
        try:
            self.driver.close()
        except:
            pass


class Product(object):

    def __init__(self, title, price, link):
        self.title = title
        self.price = price
        self.link = link
