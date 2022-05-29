from QualityTest import QualityTest
from Test.CustomerTest import CustomerTest
from Test.MarketingSupervisorTest import MarketingSupervisorTest
from Test.MarketingTest import MarketingTest
from Test.TestingSupervisorTest import TestingSupervisorTest
from Test.TestingTest import TestingTest


def customer_new_delegation(customer):
    customer.go_to_delegation()
    customer.new_delegation()
    customer.fill_delegation()
    customer.go_to_function_list()
    customer.fill_function_list()
    customer.go_to_delegation()


if __name__ == '__main__':
    c = CustomerTest()
    customer_new_delegation(c)
    ms = MarketingSupervisorTest()
    ms.distribute_delegation()
    ts = TestingSupervisorTest()
    ts.distribute_delegation()
    m = MarketingTest()
    m.audit_delegation()
    t = TestingTest()
    t.audit_delegation()
    m.generate_pricing()
    c.accept_pricing()
    m.fill_contract()
    c.check_contract()
    c.fill_contract()
    m.audit_contract()
    m.upload_contract()
    c.upload_sample()
    m.audit_sample()
    t.audit_sample()
    t.fill_solution()
    q = QualityTest()
    q.audit_solution()
    t.fill_document()
    ts.audit_report()
    c.audit_report()
