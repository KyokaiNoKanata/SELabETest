import unittest

from BeautifulReport import BeautifulReport

from Test.CustomerTest import CustomerTest
from Test.MarketingSupervisorTest import MarketingSupervisorTest
from Test.MarketingTest import MarketingTest
from Test.QualityTest import QualityTest
from Test.SignerTest import SignerTest
from Test.TestingSupervisorTest import TestingSupervisorTest
from Test.TestingTest import TestingTest


class MyTestCase(unittest.TestCase):
    def testcase1(self):
        """用户新建并填写委托"""
        c = CustomerTest()
        c.new_delegation()
        c.fill_delegation()
        c.go_to_function_list()
        c.fill_function_list()
        c.quit()
        pass

    def testcase2(self):
        """市场部主管分配人员"""
        ms = MarketingSupervisorTest()
        ms.distribute_delegation()
        ms.quit()
        pass

    def testcase3(self):
        """测试部主管分配人员"""
        ts = TestingSupervisorTest()
        ts.distribute_delegation()
        ts.quit()
        pass

    def testcase4(self):
        """市场部审核委托"""
        m = MarketingTest()
        m.audit_delegation()
        m.quit()
        pass

    def testcase5(self):
        """市场部审核委托"""
        t = TestingTest()
        t.audit_delegation()
        t.quit()
        pass

    def testcase6(self):
        """市场部生成报价"""
        m = MarketingTest()
        m.generate_pricing()
        m.quit()
        pass

    def testcase7(self):
        """客户接受报价"""
        c = CustomerTest()
        c.accept_pricing()
        c.quit()
        pass

    def testcase8(self):
        """市场部填写合同"""
        m = MarketingTest()
        m.fill_contract()
        m.quit()
        pass

    def testcase9(self):
        """客户检查合同"""
        c = CustomerTest()
        c.check_contract()
        c.quit()
        pass

    def testcase10(self):
        """客户填写合同"""
        c = CustomerTest()
        c.fill_contract()
        c.quit()
        pass

    def testcase11(self):
        """市场部审核合同"""
        m = MarketingTest()
        m.audit_contract()
        m.quit()
        pass

    def testcase12(self):
        """市场部上传合同"""
        m = MarketingTest()
        m.upload_contract()
        m.quit()
        pass

    def testcase13(self):
        """测试部主管填写项目编号"""
        ts = TestingSupervisorTest()
        ts.fill_project_id()
        ts.quit()
        pass

    def testcase14(self):
        """客户上传样品"""
        c = CustomerTest()
        c.upload_sample()
        c.quit()
        pass

    def testcase15(self):
        """市场部验收样品"""
        m = MarketingTest()
        m.audit_sample()
        m.quit()
        pass

    def testcase16(self):
        """测试部填写测试方案"""
        t = TestingTest()
        t.fill_solution()
        t.quit()
        pass

    def testcase17(self):
        """质量部审核测试方案"""
        q = QualityTest()
        q.audit_solution()
        q.quit()
        pass

    def testcase18(self):
        """测试部填写测试文档"""
        t = TestingTest()
        t.fill_document()
        t.quit()
        pass

    def testcase19(self):
        """测试部主管审核测试报告"""
        ts = TestingSupervisorTest()
        ts.audit_report()
        ts.quit()
        pass

    def testcase20(self):
        """客户审核测试报告"""
        c = CustomerTest()
        c.audit_report()
        c.quit()
        pass

    def testcase21(self):
        """授权签字人审核报告"""
        s = SignerTest()
        s.sign()
        s.quit()
        pass

    def testcase22(self):
        """测试部归档测试文档"""
        t = TestingTest()
        t.archive_report()
        t.quit()
        pass

    def testcase23(self):
        """市场部发送测试报告"""
        m = MarketingTest()
        m.send_report()
        m.quit()
        pass

    def testcase24(self):
        """客户接收测试报告"""
        c = CustomerTest()
        c.receive_report()
        c.quit()
        pass


if __name__ == '__main__':
    br = BeautifulReport(unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase))
    br.report(filename='report', description='report', report_dir='.')
