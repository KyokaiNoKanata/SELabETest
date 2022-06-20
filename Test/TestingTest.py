from Test.TestBase import TestBase


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
        # table12
        self.scroll_to_bottom()
        # 保存
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > '
                'div.ant-pro-grid-content > div > div > div.ant-pro-page-container-children-content > form > '
                'div.ant-space.ant-space-horizontal.ant-space-align-center > div:nth-child(2) > button')
        self.scroll_to_top()
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[4]')
        # 基本信息
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
        self.go_to_sidebar_item(index1=6, index2=1)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/a/button')
        # 引言
        # 标识
        self.input_into_css(css='#introduction_1-1\\ 标识', text='标识')
        # 系统概述
        self.input_into_css(css='#introduction_1-2\\ 系统概述', text='系统概述')
        # 文档概述
        self.input_into_css(css='#introduction_1-3\\ 文档概述', text='文档概述')
        # 基线
        self.input_into_css(css='#introduction_基线', text='基线')
        # 下一步
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > div > div > '
                'div:nth-child(2) > div > div > div.ant-space.ant-space-horizontal.ant-space-align-center > div > div '
                '> button.ant-btn.ant-btn-primary')
        # 引用文件
        self.input_into_css(css='#引用文件t_引用文件', text='引用文件')
        # 下一步
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > div > div > '
                'div:nth-child(2) > div > div > div.ant-space.ant-space-horizontal.ant-space-align-center > div > div '
                '> button.ant-btn.ant-btn-primary')
        # 软件测试环境
        # 硬件
        self.input_into_css(css='#软件测试环境_3-1\\ 硬件', text='硬件')
        # 软件
        self.input_into_css(css='#软件测试环境_3-2\\ 软件', text='软件')
        # 其他
        self.input_into_css(css='#软件测试环境_3-3\\ 其他', text='其他')
        # 参与组织
        self.input_into_css(css='#软件测试环境_3-4\\ 参与组织', text='参与组织')
        # 人员
        self.input_into_css(css='#软件测试环境_3-5\\ 人员', text='人员')
        # 下一步
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > div > div > '
                'div:nth-child(2) > div > div > div.ant-space.ant-space-horizontal.ant-space-align-center > div > div '
                '> button.ant-btn.ant-btn-primary')
        # 计划
        # 总体设计
        self.input_into_css(css='#计划_4-1\\ 总体设计', text='总体设计')
        # 测试级别
        self.input_into_css(css='#计划_4-1-1\\ 测试级别', text='测试级别')
        # 测试类别
        self.input_into_css(css='#计划_4-1-2\\ 测试类别', text='测试类别')
        # 一般测试条件
        self.input_into_css(css='#计划_4-1-3\\ 一般测试条件', text='一般测试条件')
        # 计划执行的测试
        self.input_into_css(css='#计划_4-2\\ 计划执行的测试', text='计划执行的测试')
        # 测试用例
        self.input_into_css(css='#计划_4-3\\ 测试用例', text='测试用例')
        # 下一步
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > div > div > '
                'div:nth-child(2) > div > div > div.ant-space.ant-space-horizontal.ant-space-align-center > div > div '
                '> button.ant-btn.ant-btn-primary')
        # 测试进度表
        # 制定测试计划
        self.input_into_css(css='#测试进度表_workQuantity1', text='制定测试计划')
        self.click_css_selector(css='#测试进度表_time1')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(2) > '
                'td.ant-picker-cell.ant-picker-cell-in-view.ant-picker-cell-today')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > '
                'td.ant-picker-cell.ant-picker-cell-start.ant-picker-cell-in-view')
        # 设计测试
        self.input_into_css(css='#测试进度表_workQuantity2', text='制定测试计划')
        self.click_css_selector(css='#测试进度表_time2')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > '
                'td.ant-picker-cell.ant-picker-cell-start.ant-picker-cell-in-view')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > '
                'td.ant-picker-cell.ant-picker-cell-start.ant-picker-cell-in-view')
        # 执行测试
        self.input_into_css(css='#测试进度表_workQuantity3', text='制定测试计划')
        self.click_css_selector(css='#测试进度表_time3')
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > '
                'td.ant-picker-cell.ant-picker-cell-start.ant-picker-cell-in-view')
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > '
                'td.ant-picker-cell.ant-picker-cell-start.ant-picker-cell-in-view')
        # 评估测试
        self.input_into_css(css='#测试进度表_workQuantity4', text='制定测试计划')
        self.click_css_selector(css='#测试进度表_time4')
        self.click_css_selector(
            css='body > div:nth-child(11) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > '
                'td.ant-picker-cell.ant-picker-cell-start.ant-picker-cell-in-view')
        self.click_css_selector(
            css='body > div:nth-child(11) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(1) > '
                'td.ant-picker-cell.ant-picker-cell-start.ant-picker-cell-in-view')
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > div > div > '
                'div:nth-child(2) > div > div > div.ant-space.ant-space-horizontal.ant-space-align-center > div > div '
                '> button.ant-btn.ant-btn-primary')
        # 需求的可追踪性
        self.input_into_css(css='#需求的可追踪性t_需求的可追踪性', text='需求的可追踪性')
        # 保存
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > div > div > '
                'div:nth-child(2) > div > div > div.ant-space.ant-space-horizontal.ant-space-align-center > div > div '
                '> div > div > div:nth-child(3) > button')
        # 提交
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > div > div > '
                'div:nth-child(2) > div > div > div.ant-space.ant-space-horizontal.ant-space-align-center > div > div '
                '> div > div > div:nth-child(4) > button')

    def fill_document(self):
        self.go_to_sidebar_item(index1=7, index2=1)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/a/button')
        # 测试用例
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/form/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[2]')
        # 测试记录
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/form/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[3]')
        # 问题清单
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/form/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[4]')
        # 测试报告
        # 测试类别
        self.input_into_css(css='#step1_测试类别_1', text='测试类别')
        self.scroll_to_bottom()
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > '
                'div.ant-pro-grid-content > div > div > div.ant-pro-page-container-children-content > '
                'div.ant-pro-card > div > div > div > div:nth-child(2) > div > div > '
                'div.ant-space.ant-space-horizontal.ant-space-align-center > div > button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[3]')
        # 项目编号
        self.input_into_css(css='#step2_项目编号', text='项目编号')
        # 提交
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/form/div[2]/div[2]/button')

    def archive_report(self):
        self.go_to_sidebar_item(index1=7, index2=5)
        self.click_css_selector(
            css='#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > '
                'div.ant-pro-page-container-children-content > div > div:nth-child(2) > div > div.ant-table-wrapper > '
                'div > div > div > div > div > table > tbody > tr > td:nth-child(6) > button')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > '
                'div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary')
