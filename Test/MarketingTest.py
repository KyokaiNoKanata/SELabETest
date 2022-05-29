from Test.TestBase import TestBase


class MarketingTest(TestBase):
    def __init__(self):
        super(MarketingTest, self).__init__()
        self.login(username='shichangbu2', password='1234')

    def go_to_delegation(self):
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/div/span')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/ul/li[5]')

    def audit_delegation(self):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/a/button')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[3]')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div')
        self.click_full_css(css='body > div:nth-child(8) > div > div > div > div.rc-virtual-list > '
                                'div.rc-virtual-list-holder > div > div > '
                                'div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option'
                                '.ant-select-item-option-active')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[2]/div/div[2]/div/div['
                  '2]/div/div/div/div/span[1]/input')
        self.click_full_css(
            css='body > div:nth-child(9) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item'
                '-option-active')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[3]/div/div[2]/div/div['
                  '2]/div/div/span/input',
            text='张三')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[3]/div/div[3]/div/div['
                  '2]/div/div/div/div/input')
        self.click_full_css(
            css='body > div:nth-child(10) > div > div > div > div > div.ant-picker-date-panel > div.ant-picker-body > '
                'table > tbody > tr:nth-child(1) > td:nth-child(2)')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[4]/button[2]')

    def go_to_generate_pricing(self):
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/div/span')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/ul/li[7]')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/a/button')

    def generate_pricing(self):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div[2]/div/form/div[14]/div['
                  '1]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div[2]/div/form/div[14]/div['
                  '2]/button')
