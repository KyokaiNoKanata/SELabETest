from Test.CustomerTest import CustomerTest
from Test.MarketingTest import MarketingTest
from Test.SignerTest import SignerTest
from Test.TestingSupervisorTest import TestingSupervisorTest
from Test.TestingTest import TestingTest

if __name__ == '__main__':
    # c = CustomerTest()
    # c.new_delegation()
    # c.fill_delegation()
    # c.go_to_function_list()
    # c.fill_function_list()
    # c.quit()
    # ms = MarketingSupervisorTest()
    # ms.distribute_delegation()
    # ms.quit()
    # ts = TestingSupervisorTest()
    # ts.distribute_delegation()
    # ts.quit()
    # m = MarketingTest()
    # m.audit_delegation()
    # m.quit()
    # t = TestingTest()
    # t.audit_delegation()
    # t.quit()
    # m = MarketingTest()
    # m.generate_pricing()
    # m.quit()
    # c = CustomerTest()
    # c.accept_pricing()
    # c.quit()
    # m = MarketingTest()
    # m.fill_contract()
    # m.quit()
    # c = CustomerTest()
    # c.check_contract()
    # c.quit()
    # c = CustomerTest()
    # c.fill_contract()
    # c.quit()
    # m = MarketingTest()
    # m.audit_contract()
    # m.quit()
    # m = MarketingTest()
    # m.upload_contract()
    # m.quit()
    # ts = TestingSupervisorTest()
    # ts.fill_project_id()
    # ts.quit()
    # c = CustomerTest()
    # c.upload_sample()
    # c.quit()
    # m = MarketingTest()
    # m.audit_sample()
    # m.quit()
    # t = TestingTest()
    # t.fill_solution()
    # t.quit()
    # q = QualityTest()
    # q.audit_solution()
    # q.quit()
    # t = TestingTest()
    # t.fill_document()
    # t.quit()
    ts = TestingSupervisorTest()
    ts.audit_report()
    ts.quit()
    c = CustomerTest()
    c.audit_report()
    c.quit()
    s = SignerTest()
    s.sign()
    s.quit()
    t = TestingTest()
    t.archive_report()
    t.quit()
    m = MarketingTest()
    m.send_report()
    m.quit()
