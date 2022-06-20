from Test.TestBase import TestBase, random_string


class MarketingTest(TestBase):
    def __init__(self):
        super(MarketingTest, self).__init__()
        self.login(username='shichangbu2', password='1234')

    def audit_delegation(self):
        self.go_to_sidebar_item(index1=1, index2=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[7]/a/button')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[4]')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div')
        self.click_css_selector(css='body > div:nth-child(8) > div > div > div > div.rc-virtual-list > '
                                    'div.rc-virtual-list-holder > div > div > '
                                    'div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option'
                                    '.ant-select-item-option-active')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[2]/div/div[2]/div/div['
                  '2]/div/div/div/div/span[1]/input')
        self.click_css_selector(
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
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div > div.ant-picker-date-panel > div.ant-picker-body > '
                'table > tbody > tr:nth-child(1) > td:nth-child(2)')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/form/div[4]/button[2]')

    def generate_pricing(self):
        self.go_to_sidebar_item(index1=1, index2=3)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[7]/a/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[2]/div/form/div[14]/div[1]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[2]/div/form/div[14]/div[2]/button')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')

    def fill_contract(self):
        self.go_to_sidebar_item(index1=1, index2=4)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[7]/a/button')
        # 保密协议
        self.input_into_css(css='#乙方法人代表', text=random_string(10))
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div['
                  '2]/button')
        # 跳转至合同
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[2]')
        # 合同
        # 合同第一页
        # 合同签订地点
        self.input_into_css(css='#step1_签订地点', text='南京')
        # 签订日期
        self.click_css_selector(css='#step1 > div:nth-child(6) > div.ant-col.ant-form-item-control > div > div > div')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div > div.ant-picker-date-panel > div.ant-picker-body > '
                'table > tbody > tr:nth-child(1) > td.ant-picker-cell.ant-picker-cell-start.ant-picker-cell-in-view')
        # 质量特性
        self.input_into_css(css='#step1_质量特性', text='质量特性')
        # 合同价款
        self.input_into_css(css='#step1_合同价款', text='1000000')
        # 完成天数
        self.input_into_css(css='#step1_完成天数', text='30')
        # 整改次数
        self.input_into_css(css='#step1_整改次数', text='1')
        # 超过天数
        self.input_into_css(css='#step1_超过天数', text='30')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div['
                  '2]/div/div/div[3]/div/div/button')
        # 签章
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div['
                  '2]/div/div/div[3]/div/div/div/div/div[2]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div['
                  '2]/div/div/div[3]/div/div/div/div/div[3]/button')

    def audit_contract(self):
        self.go_to_sidebar_item(index1=1, index2=5)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[7]/a/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[3]')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/form/div[1]/div/div/div/div['
                  '2]/div/div/span/input',
            text='通过')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/form/div[2]/div/div/div/div['
                  '2]/div/div/div/div/span[1]/input')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item'
                '-option-active')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/form/div[3]/button[2]')

    def upload_contract(self):
        self.go_to_sidebar_item(index1=1, index2=6)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[7]/button')
        self.upload_into_xpath(
            xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div/div/div/span/div[1]',
            file='C:\\Users\\Yui\\OneDrive\\图片\\Kaguya.jpg')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/button')

    def audit_sample(self):
        self.go_to_sidebar_item(index1=2, index2=2, index3=1)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div/a/button')
        self.input_into_css(css='#remark', text='通过')
        self.click_css_selector(
            css='#root > div > section > div > main > form > div > div:nth-child(6) > div > div:nth-child(4) > div > '
                'div:nth-child(2) > button')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')

    def send_report(self):
        self.go_to_sidebar_item(index1=2, index2=4, index3=2)
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-pro-grid-content > div > div > div > '
                'div:nth-child(2) > div > div.ant-table-wrapper > div > div > div > div > div > table > tbody > tr > '
                'td:nth-child(6) > button')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > '
                'div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary')
        self.wait()
