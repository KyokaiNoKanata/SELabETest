from Test.TestBase import TestBase


class TestingTest(TestBase):
    def __init__(self):
        super(TestingTest, self).__init__()
        self.login(username='ceshibu2', password='1234')

    def audit_delegation(self):
        self.go_to_sidebar_item(index1=1, index2=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[7]/a/button')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[3]')
        # table12
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > '
                'div.ant-pro-grid-content > div > div > form > div:nth-child(4) > div.ant-pro-card-body > div > div > '
                'div.ant-pro-card-body > div > div.ant-col.ant-form-item-control > div > div > div > div')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div')
        self.scroll_to_bottom()
        # 保存
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > '
                'div.ant-pro-grid-content > div > div > form > '
                'div.ant-space.ant-space-horizontal.ant-space-align-center > div:nth-child(2) > button')
        self.scroll_to_top()
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[4]')
        # 基本信息
        self.input_into_css(css='#step1_评审人', text='评审人')
        self.click_css_selector(css='#step1_time')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div > div.ant-picker-date-panel > div.ant-picker-body > '
                'table > tbody > tr:nth-child(1) > td:nth-child(2)')
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > '
                'div.ant-pro-grid-content > div > div > div.ant-pro-card > div > div > div:nth-child(2) > div > div > '
                'div.ant-space.ant-space-horizontal.ant-space-align-center > div > div > button')
        # 软件说明部分评审
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div['
                  '2]/div/div/div[5]/div/div/button[2]')
        # 软件文档集评审
        self.input_into_css(css='#step3_检查人', text='检查人')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div['
                  '2]/div/div/div[5]/div/div/button[2]')
        # 审核意见
        self.click_css_selector(css='#step4_是否通过')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item'
                '-option-active')
        self.click_full_xpath(
            xpath='//*[@id="root"]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div['
                  '2]/div/div/div[5]/div/div/div/div/div[2]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div['
                  '2]/div/div/div[5]/div/div/div/div/div[3]/button')

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
        self.go_to_sidebar_item(index1=2, index2=3, index3=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a/button')
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
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > '
                'td.ant-picker-cell.ant-picker-cell-in-view.ant-picker-cell-today')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(4)')
        # 设计测试
        self.input_into_css(css='#测试进度表_workQuantity2', text='制定测试计划')
        self.click_css_selector(css='#测试进度表_time2')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > '
                'td.ant-picker-cell.ant-picker-cell-in-view.ant-picker-cell-today')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(4)')
        # 执行测试
        self.input_into_css(css='#测试进度表_workQuantity3', text='制定测试计划')
        self.click_css_selector(css='#测试进度表_time3')
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > '
                'td.ant-picker-cell.ant-picker-cell-in-view.ant-picker-cell-today')
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(4)')
        # 评估测试
        self.input_into_css(css='#测试进度表_workQuantity4', text='制定测试计划')
        self.click_css_selector(css='#测试进度表_time4')
        self.click_css_selector(
            css='body > div:nth-child(11) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > '
                'td.ant-picker-cell.ant-picker-cell-in-view.ant-picker-cell-today')
        self.click_css_selector(
            css='body > div:nth-child(11) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(4)')
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
        self.go_to_sidebar_item(index1=2, index2=4, index3=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a/button')
        # 测试用例
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/form/div/div/div/div/div/div/div/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/form/div/div/div/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[8]/div/div[1]')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/form/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[2]')
        # 测试记录
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > '
                'div.ant-pro-grid-content > div > div > div.ant-pro-card > div > form > div > div > div > div > div > '
                'div > div > button')
        self.click_css_selector(
            css='#测试用例 > div > div > table > tbody > tr > td:nth-child(14) > div > div:nth-child(1)')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/form/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[3]')
        # 问题清单
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/form/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[4]')
        # 测试报告
        # 测试类别
        self.input_into_css(css='#step1_测试类别_1', text='测试类别')
        self.scroll_to_bottom()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[7]/div/button')
        self.input_into_css(css='#step2_样品名称', text='样品名称')
        self.input_into_css(css='#step2_版本\\/型号', text='版本')
        self.click_css_selector(css='#step2_来样日期')
        self.click_css_selector(css='body > div:nth-child(8) > div > div > div > div > div.ant-picker-date-panel > '
                                    'div.ant-picker-body > table > tbody > tr:nth-child(4) > '
                                    'td.ant-picker-cell.ant-picker-cell-in-view.ant-picker-cell-today')
        self.input_into_css(css='#step2_测试类型', text='测试类型')
        self.click_css_selector(css='#step2_测试时间')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(1) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > '
                'td.ant-picker-cell.ant-picker-cell-in-view.ant-picker-cell-today')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.ant-picker-panel-container > div > div:nth-child(2) '
                '> div > div.ant-picker-body > table > tbody > tr:nth-child(4) > td:nth-child(4)')
        self.input_into_css(css='#step2_样品状态', text='状态')
        self.input_into_css(css='#step2_样品清单', text='样品清单')
        self.input_into_css(css='#step2_测试结论', text='结论')
        self.input_into_css(css='#step2_主测人', text='主测人')
        self.click_css_selector(css='#step2_主测_日期')
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div > div.ant-picker-date-panel > div.ant-picker-body > '
                'table > tbody > tr:nth-child(4) > td.ant-picker-cell.ant-picker-cell-in-view.ant-picker-cell-today')
        self.input_into_css(css='#step2_审核人', text='审核人')
        self.click_css_selector(css='#step2_审核_日期')
        self.click_css_selector(
            css='body > div:nth-child(11) > div > div > div > div > div.ant-picker-date-panel > div.ant-picker-body > '
                'table > tbody > tr:nth-child(4) > td.ant-picker-cell.ant-picker-cell-in-view.ant-picker-cell-today')
        self.input_into_css(css='#step2_批准人', text='批准人')
        self.click_css_selector(css='#step2_批准_日期')
        self.click_css_selector(
            css='body > div:nth-child(12) > div > div > div > div > div.ant-picker-date-panel > div.ant-picker-body > '
                'table > tbody > tr:nth-child(4) > td.ant-picker-cell.ant-picker-cell-in-view.ant-picker-cell-today')
        self.input_into_css(css='#step2_电话', text='电话')
        self.input_into_css(css='#step2_传真', text='传真')
        self.input_into_css(css='#step2_地址', text='地址')
        self.input_into_css(css='#step2_邮编', text='邮编')
        self.input_into_css(css='#step2_联系人', text='联系人')
        self.input_into_css(css='#step2_E-mail', text='123@abc.com')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[7]/div[2]/button')
        self.input_into_css(css='#step3_硬件类别', text='硬件类别')
        self.input_into_css(css='#step3_硬件名称', text='硬件名称')
        self.input_into_css(css='#step3_配置', text='配置')
        self.input_into_css(css='#step3_数量', text='数量')
        # 软件环境
        self.input_into_css(
            css='#step3_软件环境 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > div > div > div '
                '> span > input',
            text='系统')
        self.input_into_css(
            css='#step3_软件环境 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > div > div > div '
                '> span > input',
            text='版本')
        self.input_into_css(
            css='#step3_软件环境 > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div > div > div '
                '> span > input',
            text='软件')
        self.input_into_css(
            css='#step3_软件环境 > div > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > div > div > div > div '
                '> span > input',
            text='软件')
        self.input_into_css(
            css='#step3_软件环境 > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > div > div > div '
                '> span > input',
            text='软件')
        self.input_into_css(
            css='#step3_软件环境 > div > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > div > div > div > div '
                '> span > input',
            text='软件')
        self.input_into_css(
            css='#step3_软件环境 > div > div > table > tbody > tr:nth-child(4) > td:nth-child(2) > div > div > div > div '
                '> span > input',
            text='软件')
        self.input_into_css(
            css='#step3_软件环境 > div > div > table > tbody > tr:nth-child(4) > td:nth-child(3) > div > div > div > div '
                '> span > input',
            text='软件')
        self.input_into_css(
            css='#step3_软件环境 > div > div > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > div > div '
                '> span > input',
            text='软件')
        self.input_into_css(
            css='#step3_软件环境 > div > div > table > tbody > tr:nth-child(5) > td:nth-child(3) > div > div > div > div '
                '> span > input',
            text='软件')
        self.input_into_css(css='#step3_网络环境', text='网络环境')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[7]/div[2]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[7]/div[2]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[7]/div[2]/button')
        self.input_into_css(css='#step6_测试执行记录', text='记录')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[7]/div[2]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[7]/div[3]/button')
        self.click_full_xpath(xpath='/html/body/div[10]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')

    def archive_report(self):
        self.go_to_sidebar_item(index1=2, index2=4, index3=3)
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-pro-grid-content > div > div > div > '
                'div:nth-child(2) > div > div.ant-table-wrapper > div > div > div > div > div > table > tbody > '
                'tr:nth-child(1) > td:nth-child(6) > a > button')
        self.scroll_to_bottom()
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-pro-grid-content > div > div > form > '
                'div:nth-child(5) > div.ant-pro-card-body.ant-pro-card-body-direction-column > div:nth-child(5) > div '
                '> div.ant-pro-card-body > div:nth-child(1) > div.ant-col.ant-form-item-control > div > div > div')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div')
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-pro-grid-content > div > div > form > '
                'div:nth-child(5) > div.ant-pro-card-body.ant-pro-card-body-direction-column > div:nth-child(5) > div '
                '> div.ant-pro-card-body > div:nth-child(2) > div.ant-col.ant-form-item-control > div > div > div')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div')
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-pro-grid-content > div > div > form > '
                'div:nth-child(5) > div.ant-pro-card-body.ant-pro-card-body-direction-column > div:nth-child(5) > div '
                '> div.ant-pro-card-body > div:nth-child(3) > div.ant-col.ant-form-item-control > div > div > div')
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div '
                '> div > div')
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-pro-grid-content > div > div > form > '
                'div.ant-space.ant-space-horizontal.ant-space-align-center > div:nth-child(2) > button')
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-pro-grid-content > div > div > form > '
                'div.ant-space.ant-space-horizontal.ant-space-align-center > div:nth-child(3) > button')
        self.click_full_xpath(xpath='/html/body/div[8]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')
