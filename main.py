import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class UiTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000")
        self.wait()

    def wait(self):
        time.sleep(1)
        self.driver.implicitly_wait(10)

    def click_full_xpath(self, xpath):
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        self.wait()

    def input_into_xpath(self, xpath, text):
        self.driver.find_element(by=By.XPATH, value=xpath).send_keys(text)
        self.wait()

    def login(self, username='kehu2', password='1234'):
        self.input_into_xpath(xpath='/html/body/div[1]/div/div[2]/div/div[2]/form/div[2]/div/div/div/span/input',
                              text=username)
        self.input_into_xpath(xpath='/html/body/div[1]/div/div[2]/div/div[2]/form/div[3]/div/div/div/span/input',
                              text=password)
        self.click_full_xpath(xpath='/html/body/div[1]/div/div[2]/div/div[2]/form/button')

    def go_to_delegation(self):
        # TO-DO fix xpath if menu is changed
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/div')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/ul/li[2]')

    def new_delegation(self, delegation_name='test'):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div['
                  '2]/div[1]/div/div[1]/button')
        self.input_into_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div/div/div/div/span/input',
                              text=delegation_name)


if __name__ == '__main__':
    test = UiTest()
    test.login()
    test.go_to_delegation()
    test.new_delegation()
