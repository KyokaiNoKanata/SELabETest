from Test.TestBase import TestBase


class SignerTest(TestBase):
    def __init__(self):
        super(SignerTest, self).__init__()
        self.login(username='33ee', password='1234')

    def sign(self):
        self.go_to_sidebar_item(index1=7, index2=4)
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-pro-grid-content > div > div > '
                'div.ant-pro-page-container-children-content > div > div:nth-child(2) > div > div.ant-table-wrapper > '
                'div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(6) > div > div > a > '
                'button')
        self.scroll_to_top()
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-head > '
                'div.ant-tabs.ant-tabs-top.ant-tabs-large.ant-card-head-tabs > div.ant-tabs-nav > '
                'div.ant-tabs-nav-wrap > div > div:nth-child(6)')
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > a > button')
