import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class UiTest(object):
    def __init__(self, deployed=False, server=''):
        # TODO: change server if deployed
        self.driver = webdriver.Chrome()
        if not deployed:
            self.driver.get("http://localhost:8000")
        else:
            self.driver.get(server)
        self.wait()

    def wait(self):
        time.sleep(1)
        self.driver.implicitly_wait(10)

    def click_full_xpath(self, xpath):
        self.wait()
        self.driver.find_element(by=By.XPATH, value=xpath).click()

    def input_into_xpath(self, xpath, text):
        self.wait()
        self.driver.find_element(by=By.XPATH, value=xpath).send_keys(text)

    def login(self, username='kehu2', password='1234'):
        self.input_into_xpath(xpath='/html/body/div[1]/div/div[2]/div/div[2]/form/div[2]/div/div/div/span/input',
                              text=username)
        self.input_into_xpath(xpath='/html/body/div[1]/div/div[2]/div/div[2]/form/div[3]/div/div/div/span/input',
                              text=password)
        self.click_full_xpath(xpath='/html/body/div[1]/div/div[2]/div/div[2]/form/button')

    def log_out(self):
        # TODO: change server if deployed
        self.driver.get('http://localhost:8000/user/login')

    def go_to_delegation(self):
        # TODO: fix xpath if menu is changed
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/div')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/ul/li[1]/span')

    def go_to_new_delegation(self):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[7]/div/div/a/button')

    def new_delegation(self, delegation_name='test'):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div['
                  '2]/div[1]/div/div[1]/button')
        self.input_into_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div/div/div/div/span/input',
                              text=delegation_name)
        self.click_full_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/button')

    def fill_delegation(self):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div/div[2]/div/div/div/label[1]')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div/div/div[2]/div/div/span/input',
            text='其他')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div[2]/div/div/span/input',
            text='测试软件')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[3]/div[2]/div/div/span/input',
            text='1.0.0')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[4]/div[2]/div/div/span/input',
            text='公司1')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[5]/div[2]/div/div/span/input',
            text='Company1')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[6]/div[2]/div/div/span/input',
            text='公司2')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[8]/div[2]/div/div/textarea',
            text='Objective User')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[9]/div[2]/div/div/div/textarea',
            text='主要用途和功能简介')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[4]/div/button')  # next step
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/label['
                  '1]/span[1]')
        self.input_into_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div['
                                    '2]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div['
                                    '1]/div/div/div[2]/div/div/div[2]/div/div/span/input', text='其他依据')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/label['
                  '3]/span[1]')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[2]/div/div/div[1]/div/div['
                  '2]/div/div/span/input',
            text='3000')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[2]/div/div/div[2]/div/div['
                  '2]/div/div/span/input',
            text='6000')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[2]/div/div/div[3]/div/div['
                  '2]/div/div/span/input',
            text='20000')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[3]/div/div[2]/div/div/div[1]/div/div['
                  '2]/div/div/div/div/span[1]/input')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[3]')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[3]/div/div[2]/div/div/div[2]/div/div['
                  '2]/div/div/div/div/span[1]/input')
        self.click_full_xpath(xpath='/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[2]')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[3]/div/div[2]/div/div/div[3]/div/div['
                  '2]/div/div/div/div/span[1]/input')
        self.click_full_xpath(xpath='/html/body/div[8]/div/div/div/div[2]/div[1]/div/div/div[5]')
        # TODO: Runtime Environment
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[1]/div/div[2]/div['
                  '4]/div/div/div/div[2]/div/div[1]/div/div/span/input',
            text='4096')


if __name__ == '__main__':
    test = UiTest()
    test.login()
    test.go_to_delegation()
    # test.new_delegation()
    test.go_to_new_delegation()
    test.fill_delegation()
