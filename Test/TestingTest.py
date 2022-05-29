from Test.TestBase import TestBase, random_string


class TestingTest(TestBase):
    def __init__(self):
        super(TestingTest, self).__init__()
        self.login(username='ceshibu2', password='1234')

    def go_to_delegation(self):
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/div')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/ul/li[6]')

    def audit_delegation(self):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/a/button')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[3]')
        # 基本信息
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[1]/form/div[2]/div/div[1]/div/div/div[1]/div/div['
                  '2]/div/div/span/input',
            text=random_string(10))
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[1]/form/div[2]/div/div[1]/div/div/div[2]/div/div['
                  '2]/div/div/span/input',
            text='1.0.0')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[1]/form/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/span/input',
            text=random_string(10))
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[1]/form/div[2]/div/div[3]/div/div/div[1]/div/div['
                  '2]/div/div/span/input',
            text='张三')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[1]/form/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div['
                  '1]/div/div/div/input')
        self.click_full_css(
            css='body > div:nth-child(8) > div > div > div > div > div.ant-picker-date-panel > div.ant-picker-body > '
                'table > tbody > tr:nth-child(1) > td:nth-child(2)')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[5]/div/div/button')
        # 软件说明部分评审
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[5]/div/div/button[2]')
        # 软件文档集评审
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[3]/form/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/span/input',
            text='张三')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[5]/div/div/button[2]')
        # 审核意见
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[4]/form/div/div/div[2]/div/div[2]/div/div/div/div/span[1]/input')
        self.click_full_css(
            css='body > div:nth-child(9) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item'
                '-option-active')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[3]/button')
