from Test.CustomerTest import CustomerTest


def customer_new_delegation(customer):
    customer.go_to_delegation()
    customer.new_delegation()
    customer.fill_delegation()
    customer.go_to_function_list()
    customer.fill_function_list()
    customer.submit_delegation()
    customer.go_to_delegation()


if __name__ == '__main__':
    c = CustomerTest()
    # ms = MarketingSupervisorTest()
    # m = MarketingTest()
    # t = TestingTest()
    # ts = TestingSupervisorTest()
    # customer_new_delegation(c)
    # ms.distribute_delegation()
    # ts.distribute_delegation()
    # m.audit_delegation()
    # t.audit_delegation()
    # m.generate_pricing()
    # c.accept_pricing()
    # m.fill_contract()
    # c.check_contract()
    c.fill_contract()
