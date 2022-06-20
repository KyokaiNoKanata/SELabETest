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
        self.go_to_sidebar_item(index1=3, index2=8)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/a/button')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div[2]/div/form/div[9]/div['
                  '2]/div/div/span/input',
            text='kehu2')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div[2]/div/form/div[14]/div['
                  '1]/button')

    def new_delegation(self, delegation_name=random_string(10)):
        self.go_to_sidebar_item(index1=3, index2=1)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div['
                  '2]/div[1]/div/div[1]/button')
        self.input_into_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div/div/div/div/span/input',
                              text=delegation_name)
        self.click_full_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/button')

    def fill_delegation(self):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/a/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div/div[2]/div/div/div/label[1]')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div/div/div[2]/div/div/span/input',
            text='其他')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div[2]/div/div/span/input',
            text='测试软件')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[3]/div[2]/div/div/span/input',
            text='1.0.0')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[4]/div[2]/div/div/span/input',
            text='公司1')
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[5]/div[2]/div/div/span/input',
            text='Company1')
        # 单位性质
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[6]/div[2]/div/div/span/input',
            text='公司2')
        # 软件用户对象描述
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[8]/div[2]/div/div/textarea',
            text='Objective User')
        # 主要功能及用途简介
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[1]/form/div[9]/div[2]/div/div/div/textarea',
            text='主要用途和功能简介')
        # 下一步
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[4]/div/button')
        # 测试依据
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/label['
                  '1]/span[1]/input')
        # 测试依据-其他
        self.input_into_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div['
                                    '2]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div['
                                    '1]/div/div/div[2]/div/div/div[2]/div/div/span/input',
                              text='其他依据')
        # 需要测试的技术指标
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/label['
                  '3]/span[1]')
        # 功能数
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[2]/div/div/div[1]/div/div['
                  '2]/div/div/span/input',
            text='3000')
        # 功能点数
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[2]/div/div/div[2]/div/div['
                  '2]/div/div/span/input',
            text='6000')
        # 代码行数
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[2]/div/div/div[3]/div/div['
                  '2]/div/div/span/input',
            text='20000')
        # 软件类型
        self.click_css_selector(css='#step2_软件类型')
        self.click_css_selector(
            css='body > div:nth-child(8) > div > div > div > div > div > div.ant-select-tree-list > '
                'div.ant-select-tree-list-holder > div > div > div:nth-child(3) > '
                'span.ant-select-tree-node-content-wrapper.ant-select-tree-node-content-wrapper-normal')
        # 运行环境
        # 内存要求
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[1]/div/div[2]/div['
                  '4]/div/div/div/div[2]/div/div[1]/div/div/span/input',
            text='4096')
        # 服务器端
        # 架构
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div['
                                    '1]/div[2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div['
                                    '2]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/label[1]/span[1]')
        # 内存要求
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div['
                  '2]/div/div/div[3]/div/div[2]/div/div[1]/div/div/span/input',
            text='4096')
        # 硬盘要求
        self.input_into_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div['
                                    '2]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div['
                                    '2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div['
                                    '1]/div/div/span/input',
                              text='4096')
        # 软件
        # 操作系统
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div['
                  '2]/div[1]/div/div[1]/div/div[2]/div/div/span/input',
            text='Windows 11')
        # 版本
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div['
                  '2]/div[1]/div/div[2]/div/div[2]/div/div/span/input',
            text='22H2')
        # 编程语言
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div['
                  '2]/div[1]/div/div[3]/div/div[2]/div[1]/div/span/input',
            text='C++')
        # 数据库
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div['
                  '2]/div[1]/div/div[4]/div/div[2]/div/div/span/input',
            text='DB')
        # 中间件
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div['
                  '2]/div[1]/div/div[5]/div/div[2]/div/div/span/input',
            text='Middleware')
        # 其他支撑软件
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div['
                  '2]/div[1]/div/div[6]/div/div[2]/div/div/span/input',
            text='Others')
        # 构架
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div['
                  '2]/div[2]/div[2]/div/div/div/label[1]/span[1]')
        # 网络环境
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[3]/div/div[2]/div/div/div['
                  '1]/div/span/input',
            text='net')
        # 文档材料
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[5]/div[2]/div[2]/div/div[2]/div[1]/div/div['
                  '1]/div/textarea',
            text='文档材料')
        # 样品保存期满
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[5]/div[2]/div[3]/div/div[2]/div/div/div['
                  '1]/div/div/div')
        self.click_css_selector(
            css='body > div:nth-child(9) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > '
                'div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item'
                '-option-active')
        # 下一步
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[4]/div[2]/button')
        # 委托单位信息
        # 电话
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[1]/div/div/div[2]/div[1]/div[2]/div/div/span/input',
            text='123456789')
        # 传真
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[1]/div/div/div[2]/div[2]/div[2]/div/div/span/input',
            text='123456789')
        # 地址
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[1]/div/div/div[2]/div[3]/div[2]/div/div/span/input',
            text='地址')
        # 邮编
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[1]/div/div/div[2]/div[4]/div[2]/div/div/span/input',
            text='123456')
        # 联系人
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[1]/div/div/div[2]/div[5]/div[2]/div/div/span/input',
            text='联系人')
        # 手机
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[1]/div/div/div[2]/div[6]/div[2]/div/div/span/input',
            text='123456789')
        # E-mail
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[1]/div/div/div[2]/div[7]/div[2]/div/div/span/input',
            text='123@abc.com')
        # 网址
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[1]/div/div/div[2]/div[8]/div[2]/div['
                  '1]/div/span/input',
            text='www.baidu.com')
        # 密级
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[2]/div/div[1]/div[2]/div/div/div/div')
        self.click_css_selector(
            css='body > div:nth-child(10) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div '
                '> div > div:nth-child(1)')
        # 查杀病毒
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div/div')
        self.click_css_selector(
            css='body > div:nth-child(11) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div '
                '> div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select'
                '-item-option-active')
        # 所用查杀工具
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[2]/div/div[3]/div/div/div[2]/div/div/span/input',
            text='360')
        # 材料检查
        # 测试样品
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[3]/div[2]/div/div/div[1]/div/div['
                  '2]/div/div/div/label[2]/span[1]/input')
        # 需求文档
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[3]/div[2]/div/div/div[2]/div/div['
                  '2]/div/div/div/label[1]/span[1]/input')
        # 用户文档
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[3]/div[2]/div/div/div[3]/div/div['
                  '2]/div/div/div/label[1]/span[1]/input')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[3]/div[2]/div/div/div[4]/div/div['
                  '2]/div/div/div/label[1]/span[1]')
        # 测试项目编号
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[4]/div/div/div[2]/div/div/span/input',
            text=random_string(10))
        # 备注
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[5]/div/div/div[2]/div[1]/div/textarea',
            text='多放辣椒')
        # 委托人（签字）
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[6]/div/div/div/div[1]/div/div[2]/div/div/span/input',
            text='张三')
        # 保存
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[4]/div[2]/button')

    def fill_function_list(self):
        # 保存
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/form/div['
                  '4]/div[2]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/form/div['
                  '4]/div[3]/button')

    def check_contract(self):
        self.go_to_sidebar_item(index1=4, index2=4)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div/a/button')
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
        self.go_to_sidebar_item(index1=4, index2=3)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div/a/button')
        # 保密协议
        self.scroll_to_bottom()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '1]/form/div/div[2]/button')
        self.scroll_to_top()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div')
        # 合同第一页
        self.scroll_to_bottom()
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '1]/div/div/div/div[2]/div/div/div[3]/div/div/button')
        # 签章
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div[2]/button')
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div['
                  '1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div[3]/button')

    def upload_sample(self):
        self.go_to_sidebar_item(index1=5, index2=1)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
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
        self.go_to_sidebar_item(index1=7, index2=3)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div/a/button')
        self.scroll_to_top()
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[6]')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/a/button')
