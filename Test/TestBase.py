import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


class TestBase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000")
        self.wait()

    def wait(self):
        time.sleep(1)
        self.driver.implicitly_wait(20)

    def scroll_to_top(self):
        self.wait()
        js_top = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js_top)

    def click_full_xpath(self, xpath):
        self.wait()
        self.driver.find_element(by=By.XPATH, value=xpath).click()

    def click_css_selector(self, css):
        self.wait()
        self.driver.find_element(by=By.CSS_SELECTOR, value=css).click()

    def input_into_xpath(self, xpath, text):
        self.wait()
        self.driver.find_element(by=By.XPATH, value=xpath).clear()
        self.driver.find_element(by=By.XPATH, value=xpath).send_keys(text)

    def go_to_sidebar_item(self, index1, index2):
        self.click_full_xpath(xpath=f'/html/body/div[1]/div/section/aside/div/div[1]/ul/li[{index1}]/div/span')
        self.click_full_xpath(xpath=f'/html/body/div[1]/div/section/aside/div/div[1]/ul/li[{index1}]/ul/li[{index2}]')

    def login(self, username='kehu2', password='1234'):
        self.input_into_xpath(xpath='/html/body/div[1]/div/div[2]/div/div[2]/form/div[2]/div/div/div/span/input',
                              text=username)
        self.input_into_xpath(xpath='/html/body/div[1]/div/div[2]/div/div[2]/form/div[3]/div/div/div/span/input',
                              text=password)
        self.click_full_xpath(xpath='/html/body/div[1]/div/div[2]/div/div[2]/form/button')

    def log_out(self):
        # TODO: change server if deployed
        self.driver.get('http://localhost:8000/user/login')
