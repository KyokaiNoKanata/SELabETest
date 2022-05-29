from Test.TestBase import TestBase, random_string


class TestingTest(TestBase):
    def __init__(self):
        super(TestingTest, self).__init__()
        self.login(username='ceshibu2', password='1234')

    def audit_delegation(self):
        self.go_to_sidebar_item(index1=3, index2=6)
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
        self.click_css_selector(
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
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item'
                '-option-active')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[3]/button')

    def audit_sample(self):
        self.go_to_sidebar_item(index1=5, index2=3)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/a/button')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/form/div/div[7]/div/div[2]/div[2]/div/div/textarea',
            text='审核通过')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/form/div/div[7]/div/div[3]/div/div[2]/button')

    def fill_solution(self):
        self.go_to_sidebar_item(index1=6, index2=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/a/button')
        # 引言
        # 标识
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div/div/div[2]/div/div/div[1]/form/div[1]/div['
                  '2]/div/div/textarea',
            text='引言')
        # 系统概述
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div/div/div[2]/div/div/div[1]/form/div[2]/div['
                  '2]/div/div/textarea',
            text='系统概述')
        # 文档概述
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div/div/div[2]/div/div/div[1]/form/div[3]/div['
                  '2]/div/div/textarea',
            text='文档概述')
        # 基线
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div/div/div[2]/div/div/div[1]/form/div[4]/div['
                  '2]/div/div/textarea',
            text='基线')
        # 下一步
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div/div/div[2]/div/div/div[6]/div/div/button[2]')
        # 引用文件
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div/div/div[2]/div/div/div[2]/form/div/div['
                  '2]/div/div/textarea',
            text='引用文件')
        # 下一步
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[6]/div/div/button[2]')
        # 软件测试环境
        # 硬件
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[3]/form/div[1]/div['
                  '2]/div/div/textarea',
            text='硬件')
        # 软件
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[3]/form/div[2]/div['
                  '2]/div/div/textarea',
            text='软件')
        # 其他
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[3]/form/div[3]/div['
                  '2]/div/div/textarea',
            text='其他')
        # 参与组织
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[3]/form/div[4]/div['
                  '2]/div/div/textarea',
            text='参与组织')
        # 人员
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[3]/form/div[5]/div['
                  '2]/div/div/textarea',
            text='人员')
        # 下一步
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[6]/div/div/button[2]')
        # 计划
        # 总体设计
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[4]/form/div[1]/div['
                  '2]/div/div/textarea',
            text='总体设计')
        # 测试级别
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[4]/form/div[2]/div['
                  '2]/div/div/textarea',
            text='测试级别')
        # 测试类别
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[4]/form/div[3]/div['
                  '2]/div/div/textarea',
            text='测试类别')
        # 一般测试条件
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[4]/form/div[4]/div['
                  '2]/div/div/textarea',
            text='一般测试条件')
        # 计划执行的测试
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[4]/form/div[5]/div['
                  '2]/div/div/textarea',
            text='计划执行的测试')
        # 测试用例
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[4]/form/div[6]/div['
                  '2]/div/div/textarea',
            text='测试用例')
        # 下一步
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[6]/div/div/button[2]')
        # 测试进度表
        # 制定测试计划
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[5]/form/div[1]/div['
                  '2]/div[1]/div/div[2]/div/div/span/input',
            text='111')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[5]/form/div[1]/div['
                  '2]/div[2]/div/div[2]/div/div/div/div[1]/input')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > td:nth-child(4)')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(5)')
        # 设计测试
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[5]/form/div[2]/div['
                  '2]/div[1]/div/div[2]/div/div/span/input',
            text='222')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[5]/form/div[2]/div['
                  '2]/div[2]/div/div[2]/div/div/div/div[1]/input')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > td:nth-child(4)')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(5)')
        # 执行测试
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[5]/form/div[3]/div['
                  '2]/div[1]/div/div[2]/div/div/span/input',
            text='222')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[5]/form/div[3]/div['
                  '2]/div[2]/div/div[2]/div/div/div/div[1]/input')
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > td:nth-child(4)')
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(5)')
        # 评估测试
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[5]/form/div[4]/div['
                  '2]/div[1]/div/div[2]/div/div/span/input',
            text='222')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[5]/form/div[4]/div['
                  '2]/div[2]/div/div[2]/div/div/div/div[1]/input')
        self.click_css_selector(
            css='body > div:nth-child(11) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > td:nth-child(4)')
        self.click_css_selector(
            css='body > div:nth-child(11) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(5)')
        # 保存
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[6]/div/div/div/div/div['
                  '3]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[6]/div/div/div/div/div['
                  '3]/button')
        # 提交
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div/div/div[2]/div/div/div[6]/div/div/div/div/div['
                  '4]/button')
