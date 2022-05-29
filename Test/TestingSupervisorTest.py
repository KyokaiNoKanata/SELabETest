from Test.TestBase import TestBase


class TestingSupervisorTest(TestBase):
    def __init__(self):
        super(TestingSupervisorTest, self).__init__()
        self.login(username='q1w3', password='1234')

    def distribute_delegation(self):
        self.go_to_sidebar_item(index1=3, index2=4)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div/button')
        self.input_into_xpath(
            xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div/div/div/div/div/div/span[1]/input',
            text='测试部员工2')
        self.click_full_xpath(xpath='/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/button')

    def audit_report(self):
        self.go_to_sidebar_item(index1=7, index2=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div/a/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[5]')
        # 测试报告检查表
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/form/div['
                  '4]/div[1]/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[6]')
        # 审核
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/a/button')
