from Test.CustomerTest import CustomerTest


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
    customer = CustomerTest()
    customer_new_delegation(customer)
