from Test.TestBase import TestBase


class SignerTest(TestBase):
    def __init__(self):
        super(SignerTest, self).__init__()
        self.login(username='33ee', password='1234')

    def sign(self):
        self.go_to_sidebar_item(index1=1, index2=4, index3=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a/button')
        self.scroll_to_top()
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[5]')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[2]/div/div/div/div['
                  '2]/div/div/div/div/span[1]/input')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item'
                '-option-active')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[3]/button[2]')
