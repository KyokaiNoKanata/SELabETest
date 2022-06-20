from Test.TestBase import TestBase, random_string


class TestingSupervisorTest(TestBase):
    def __init__(self):
        super(TestingSupervisorTest, self).__init__()
        self.login(username='q1w3', password='1234')

    def distribute_delegation(self):
        self.go_to_sidebar_item(index1=1, index2=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[7]/div/div/button')
        self.input_into_xpath(
            xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div/div/div/div/div/div/span[1]/input',
            text='测试部员工2')
        self.click_full_xpath(xpath='/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/button')

    def audit_report(self):
        self.go_to_sidebar_item(index1=2, index2=4, index3=3)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[5]')
        # 测试报告检查表
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div['
                  '1]/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[7]/div')
        self.click_css_selector(css='#pass')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item'
                '-option-active > div')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[3]/button[2]')

    def fill_project_id(self):
        self.go_to_sidebar_item(index1=1, index2=4)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[7]/a/button')
        self.input_into_css(css='#projectId', text=random_string(10))
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div[2]/main/form/div[2]/button[2]')
