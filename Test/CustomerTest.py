from Test.TestBase import TestBase, random_string


class CustomerTest(TestBase):
    def __init__(self):
        super(CustomerTest, self).__init__()
        self.login(username='kehu2', password='1234')

    def go_to_function_list(self):
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[2]')

    def accept_pricing(self):
        self.go_to_sidebar_item(index1=1, index2=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[8]/a/button')
        self.input_into_css(css='#sign', text='张三')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[2]/div/form/div[14]/div[1]/button')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')

    def new_delegation(self, delegation_name=random_string(10)):
        self.go_to_sidebar_item(index1=1, index2=1)
        self.click_full_xpath(
            xpath='//*[@id="root"]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div['
                  '1]/div/div[1]/button')
        self.input_into_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div/div/div/div/span/input',
                              text=delegation_name)
        self.click_full_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/button')

    def fill_delegation(self):
        self.click_css_selector(
            css='#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > '
                'div:nth-child(2) > div > div.ant-table-wrapper > div > div > div > div > div > table > tbody > '
                'tr:nth-child(1) > td:nth-child(6) > a > button')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div/div/div[2]/div/div/span/input',
            text='其他')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div[2]/div/div/span/input',
            text='测试软件')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[3]/div[2]/div/div/span/input',
            text='1.0.0')
        # 委托单位
        self.input_into_css(css='#step1_委托单位Ch', text='公司1')
        # 委托单位（英文）
        self.input_into_css(css='#step1_委托单位En', text='Company')
        # 开发单位
        self.input_into_css(css='#step1_开发单位', text='公司2')
        # 软件用户对象描述
        self.input_into_css(css='#step1_软件用户对象描述', text='测试软件')
        # 主要功能及用途简介
        self.input_into_css(css='#step1_主要功能及用途简介（限200字）', text='测试软件')
        # 下一步
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[4]/div/button')
        # 功能数
        self.input_into_css(css='#step2_功能数', text='1')
        # 功能点数
        self.input_into_css(css='#step2_功能点数', text='1')
        # 代码行数
        self.input_into_css(css='#step2_代码行数', text='1')
        # 软件类型
        self.click_css_selector(css='#step2_软件类型')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div > div > div.ant-select-tree-list > '
                'div.ant-select-tree-list-holder > div > div > div:nth-child(3) > '
                'span.ant-select-tree-node-content-wrapper.ant-select-tree-node-content-wrapper-normal')
        # 运行环境
        # 内存要求
        self.input_into_css(css='#step2_客户端内存要求', text='1')
        # 服务器端
        # 架构
        self.click_css_selector(css='#step2_架构 > label:nth-child(1) > span.ant-checkbox > input')
        # 内存要求
        self.input_into_css(css='#step2_服务器端内存要求', text='4096')
        # 硬盘要求
        self.input_into_css(css='#step2_服务器端硬盘要求', text='4096')
        # 软件
        # 操作系统
        self.input_into_css(css='#step2_操作系统', text='Windows 11')
        # 版本
        self.input_into_css(css='#step2_版本', text='22H2')
        # 编程语言
        self.input_into_css(css='#step2_编程语言', text='C++')
        # 数据库
        self.input_into_css(css='#step2_数据库', text='MySQL')
        # 中间件
        self.input_into_css(css='#step2_中间件', text='中间件')
        # 其他支撑软件
        self.input_into_css(css='#step2_其他支撑软件', text='支撑软件')
        # 构架
        self.click_css_selector(css='#step2_构架 > label:nth-child(1) > span.ant-checkbox')
        # 网络环境
        self.input_into_css(css='#step2_网络环境', text='网络环境')
        # 文档资料
        self.input_into_css(css='#step2_文档资料', text='文档资料')
        # 样品保存期满
        self.click_css_selector(css='#step2_提交的样品')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item'
                '-option-active')
        # 下一步
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '2]/div/div/div/div[2]/div/div/div[4]/div[2]/button')
        # 委托单位信息
        # 电话
        self.input_into_css(css='#step3_委托单位_电话', text='123456789')
        # 传真
        self.input_into_css(css='#step3_委托单位_传真', text='123456789')
        # 地址
        self.input_into_css(css='#step3_委托单位_地址', text='南京大学')
        # 邮编
        self.input_into_css(css='#step3_委托单位_邮编', text='123456789')
        # 联系人
        self.input_into_css(css='#step3_委托单位_联系人', text='123456789')
        # 手机
        self.input_into_css(css='#step3_委托单位_手机', text='123456789')
        # E-mail
        self.input_into_css(css='#step3_委托单位_Email', text='123@abc.com')
        # 网址
        self.input_into_css(css='#step3_委托单位_网址', text='www.nju.edu.cn')
        # 密级
        self.click_css_selector(css='#step3_密级')
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div '
                '> div > div:nth-child(1)')
        # 查杀病毒
        self.click_css_selector(css='#step3_查杀病毒')
        self.click_css_selector(
            css='body > div:nth-child(11) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div '
                '> div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select'
                '-item-option-active')
        # 所用查杀工具
        self.input_into_css(css='#step3_所用查杀工具', text='360')
        # 材料检查
        # 测试样品
        self.click_css_selector(css='#step3_测试样品 > label:nth-child(1) > span.ant-checkbox')
        # 需求文档
        self.click_css_selector(css='#step3_需求文档 > label:nth-child(1) > span.ant-checkbox')
        # 用户文档
        self.click_css_selector(css='#step3_用户文档 > label:nth-child(1) > span.ant-checkbox')
        # 操作文档
        self.click_css_selector(css='#step3_操作文档 > label:nth-child(1) > span.ant-checkbox')
        # 委托人（签字）
        self.input_into_css(css='#step3_委托人（签字）', text='委托人')
        # 保存
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > '
                'div.ant-pro-grid-content > div > div > div.ant-pro-card > div > div > div > div:nth-child(2) > div > '
                'div > div.ant-space.ant-space-horizontal.ant-space-align-center > div:nth-child(2) > button')

    def fill_function_list(self):
        # 保存
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > '
                'div.ant-pro-grid-content > div > div > form > '
                'div.ant-space.ant-space-horizontal.ant-space-align-center > div:nth-child(2) > button')
        self.click_css_selector(
            css='#root > div > section > div > main > div > div.ant-card-body > div > div > div > '
                'div.ant-pro-grid-content > div > div > form > '
                'div.ant-space.ant-space-horizontal.ant-space-align-center > div:nth-child(3) > button')

    def check_contract(self):
        self.go_to_sidebar_item(index1=1, index2=4)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[8]/a/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[3]')
        # 意见
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/form/div[1]/div/div/div/div['
                  '2]/div/div/span/input',
            text='这是好的')
        # 是否通过
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/form/div[2]/div/div/div/div['
                  '2]/div/div/div/div/span[1]/input')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item'
                '-option-active')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/form/div[3]/button[2]')

    def fill_contract(self):
        self.go_to_sidebar_item(index1=1, index2=3)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[8]/a/button')
        # 保密协议
        self.scroll_to_bottom()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div['
                  '2]/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div')
        # 合同第一页
        self.scroll_to_bottom()
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

    def upload_sample(self):
        self.go_to_sidebar_item(index1=2, index2=2, index3=2)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div/button')
        self.upload_into_xpath(
            xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/span/div[1]/span/button',
            file='C:\\Users\\Yui\\OneDrive\\图片\\Kaguya.jpg')
        self.input_into_xpath(
            xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div/span/input',
            text='HouraisanKaguya')
        self.input_into_xpath(
            xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/div/span/input',
            text='处理方式')
        self.input_into_xpath(
            xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/div/span/input',
            text='线上')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/button')

    def audit_report(self):
        self.go_to_sidebar_item(index1=2, index2=4, index3=2)
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

    def receive_report(self):
        self.go_to_sidebar_item(index1=2, index2=4, index3=3)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/button')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > '
                'div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary')
