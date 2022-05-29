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
    # customer_new_delegation(c)
    # ms = MarketingSupervisorTest()
    # ms.go_to_delegation()
    # ms.distribute_delegation()
    # ts = TestingSupervisorTest()
    # ts.go_to_delegation()
    # ts.distribute_delegation()
    # m = MarketingTest()
    # m.go_to_delegation()
    # m.audit_delegation()
    # t = TestingTest()
    # t.go_to_delegation()
    # t.audit_delegation()
    # m.go_to_generate_pricing()
    # m.generate_pricing()
    c.go_to_pricing()
    c.accept_pricing()
