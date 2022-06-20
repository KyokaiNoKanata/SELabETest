from Test.TestBase import TestBase


class QualityTest(TestBase):
    def __init__(self):
        super(QualityTest, self).__init__()
        self.login(username='zhiliangbu2', password='1234')

    def audit_solution(self):
        self.go_to_sidebar_item(index1=2, index2=3, index3=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[2]')
        # 测试类别
        self.input_into_css(css='#测试类别', text='测试类别')
        # 保存
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/form/div['
                  '4]/div/div/div[1]/button')
        # 通过
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/form/div['
                  '4]/div/div/div[3]/button')
