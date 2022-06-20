from Test.TestBase import TestBase


class MarketingSupervisorTest(TestBase):
    def __init__(self):
        super(MarketingSupervisorTest, self).__init__()
        self.login(username='asdasdas1', password='1234')

    def distribute_delegation(self):
        self.go_to_sidebar_item(index1=1, index2=2)
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-pro-grid-content > div > div > div > '
                'div:nth-child(2) > div > div.ant-table-wrapper > div > div > div > div > div > table > tbody > '
                'tr:nth-child(1) > td:nth-child(7) > div > div > button')
        self.input_into_xpath(
            xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div/div/div/div/div/div/span[1]/input',
            text='市场部员工2')
        self.click_full_xpath(xpath='/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[1]')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/button')
