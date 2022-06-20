import unittest

import BeautifulReport


def get_result():
    test_suite = unittest.TestSuite()
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))
    res = BeautifulReport.BeautifulReport(test_suite)
    res.report(filename='report', description='测试报告', log_path=None)


class Test(unittest.TestCase):
    def setUp(self):
        ...
