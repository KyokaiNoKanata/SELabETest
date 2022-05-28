from Test.TestBase import TestBase


class MarketingSupervisorTest(TestBase):
    def __init__(self):
        super().__init__()
        self.login(username='marketing_department_manger', password='1234')
