from Test.TestingSupervisorTest import TestingSupervisorTest


def customer_new_delegation(customer):
    customer.go_to_delegation()
    customer.new_delegation()
    customer.go_to_new_delegation()
    customer.fill_delegation()
    customer.go_to_function_list()
    customer.fill_function_list()
    customer.submit_delegation()
    customer.go_to_delegation()


if __name__ == '__main__':
    # c = CustomerTest()
    # customer_new_delegation(c)
    # ms = MarketingSupervisorTest()
    # ms.go_to_delegation()
    # ms.distribute_delegation()
    ts = TestingSupervisorTest()
    ts.go_to_delegation()
    ts.distribute_delegation()
