from Test.TestBase import TestBase


class MarketingSupervisorTest(TestBase):
    def __init__(self):
        super(MarketingSupervisorTest, self).__init__()
        self.login(username='asdasdas1', password='1234')

    def go_to_delegation(self):
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/div/span')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/ul/li[3]')

    def distribute_delegation(self):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div/button')
        self.input_into_xpath(
            xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div/div/div/div/div/div/span[1]/input',
            text='市场部员工2')
        self.click_full_xpath(xpath='/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[1]')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/button')
