import unittest
import timeout_decorator
import pypara.dcc as module_0

class Test_Dcc_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            date_0 = None
            decimal_0 = module_0.dcfc_30_360_us(date_0, date_0, date_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
