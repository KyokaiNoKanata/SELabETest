from Test.TestBase import TestBase, random_string, js_top


class CustomerTest(TestBase):
    def __init__(self, deployed=False, server=''):
        # TODO: change server if deployed
        super().__init__(deployed, server)

    def go_to_delegation(self):
        # TODO: fix xpath if menu is changed
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/div')
        self.click_full_xpath(xpath='/html/body/div[1]/div/section/aside/div/div[1]/ul/li[3]/ul/li[1]/span')

    def go_to_new_delegation(self):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div['
                  '2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/a/button')

    def go_to_function_list(self):
        self.driver.execute_script(js_top)
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[2]')

    def new_delegation(self, delegation_name=random_string(10)):
        self.click_full_xpath(

            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div['
                  '2]/div[1]/div/div[1]/button')
        self.input_into_xpath(xpath='/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div/div/div/div/span/input',
                              text=delegation_name)
        self.click_full_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/button')

    def fill_delegation(self):
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
                                    '1]/div/div/div[2]/div/div/div[2]/div/div/span/input', text='其他依据')
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
        # 系统软件
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[3]/div/div[2]/div/div/div[1]/div/div['
                  '2]/div/div/div/div')
        self.click_full_xpath(xpath='/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[3]')
        # 支持软件
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[3]/div/div[2]/div/div/div[2]/div/div['
                  '2]/div/div/div/div')
        self.click_full_xpath(xpath='/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[2]')
        # 应用软件
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[3]/div/div[2]/div/div/div[3]/div/div['
                  '2]/div/div/div/div')
        self.click_full_xpath(xpath='/html/body/div[7]/div/div/div/div[2]/div[1]/div/div/div[5]')
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
                  '2]/div[1]/div/div[4]/div/div[2]/div/div/span/input', text='DB')
        # 中间件
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div['
                  '2]/div[1]/div/div[5]/div/div[2]/div/div/span/input', text='Middleware')
        # 其他支撑软件
        self.input_into_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div['
                  '2]/div[1]/div/div[6]/div/div[2]/div/div/span/input', text='Others')
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
        self.click_full_xpath(xpath='/html/body/div[8]/div/div/div/div[2]/div[1]/div/div/div[1]')
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
        self.click_full_xpath(xpath='/html/body/div[9]/div/div/div/div[2]/div[1]/div/div/div[1]')
        # 查杀病毒
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div[2]/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div['
                  '2]/div/div/div/div[2]/div/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div/div')
        self.click_full_xpath(xpath='/html/body/div[10]/div/div/div/div[2]/div[1]/div/div/div[1]')
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

    def submit_delegation(self):
        self.click_full_xpath(
            xpath='/html/body/div[1]/div/section/div/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/form/div['
                  '4]/div[3]/button')
