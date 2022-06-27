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
    @staticmethod
    def testcase01():
        """用户新建并填写委托"""
        c = CustomerTest()
        c.new_delegation()
        c.fill_delegation()
        c.go_to_function_list()
        c.fill_function_list()
        c.quit()
        pass

    @staticmethod
    def testcase02():
        """市场部主管分配人员"""
        ms = MarketingSupervisorTest()
        ms.distribute_delegation()
        ms.quit()
        pass

    @staticmethod
    def testcase03():
        """测试部主管分配人员"""
        ts = TestingSupervisorTest()
        ts.distribute_delegation()
        ts.quit()
        pass

    @staticmethod
    def testcase04():
        """市场部审核委托"""
        m = MarketingTest()
        m.audit_delegation()
        m.quit()
        pass

    @staticmethod
    def testcase05():
        """测试部审核委托"""
        t = TestingTest()
        t.audit_delegation()
        t.quit()
        pass

    @staticmethod
    def testcase06():
        """市场部生成报价"""
        m = MarketingTest()
        m.generate_pricing()
        m.quit()
        pass

    @staticmethod
    def testcase07():
        """客户接受报价"""
        c = CustomerTest()
        c.accept_pricing()
        c.quit()
        pass

    @staticmethod
    def testcase08():
        """市场部填写合同"""
        m = MarketingTest()
        m.fill_contract()
        m.quit()
        pass

    @staticmethod
    def testcase09():
        """客户检查合同"""
        c = CustomerTest()
        c.check_contract()
        c.quit()
        pass

    @staticmethod
    def testcase10():
        """客户填写合同"""
        c = CustomerTest()
        c.fill_contract()
        c.quit()
        pass

    @staticmethod
    def testcase11():
        """市场部审核合同"""
        m = MarketingTest()
        m.audit_contract()
        m.quit()
        pass

    @staticmethod
    def testcase12():
        """市场部上传合同"""
        m = MarketingTest()
        m.upload_contract()
        m.quit()
        pass

    @staticmethod
    def testcase13():
        """测试部主管填写项目编号"""
        ts = TestingSupervisorTest()
        ts.fill_project_id()
        ts.quit()
        pass

    @staticmethod
    def testcase14():
        """客户上传样品"""
        c = CustomerTest()
        c.upload_sample()
        c.quit()
        pass

    @staticmethod
    def testcase15():
        """市场部验收样品"""
        m = MarketingTest()
        m.audit_sample()
        m.quit()
        pass

    @staticmethod
    def testcase16():
        """测试部填写测试方案"""
        t = TestingTest()
        t.fill_solution()
        t.quit()
        pass

    @staticmethod
    def testcase17():
        """质量部审核测试方案"""
        q = QualityTest()
        q.audit_solution()
        q.quit()
        pass

    @staticmethod
    def testcase18():
        """测试部填写测试文档"""
        t = TestingTest()
        t.fill_document()
        t.quit()
        pass

    @staticmethod
    def testcase19():
        """测试部主管审核测试报告"""
        ts = TestingSupervisorTest()
        ts.audit_report()
        ts.quit()
        pass

    @staticmethod
    def testcase20():
        """客户审核测试报告"""
        c = CustomerTest()
        c.audit_report()
        c.quit()
        pass

    @staticmethod
    def testcase21():
        """授权签字人审核报告"""
        s = SignerTest()
        s.sign()
        s.quit()
        pass

    @staticmethod
    def testcase22():
        """测试部归档测试文档"""
        t = TestingTest()
        t.archive_report()
        t.quit()
        pass

    @staticmethod
    def testcase23():
        """市场部发送测试报告"""
        m = MarketingTest()
        m.send_report()
        m.quit()
        pass

    @staticmethod
    def testcase24():
        """客户接收测试报告"""
        c = CustomerTest()
        c.receive_report()
        c.quit()
        pass


if __name__ == '__main__':
    br = BeautifulReport(unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase))
    br.report(filename='report', description='report', report_dir='.')
