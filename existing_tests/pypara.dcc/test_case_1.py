import unittest
import timeout_decorator
import pypara.dcc as module_0

class Test_Dcc_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            date_0 = None
            decimal_0 = module_0.dcfc_act_365_f(date_0, date_0, date_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
