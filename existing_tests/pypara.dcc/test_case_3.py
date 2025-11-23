import unittest
import timeout_decorator
import pypara.dcc as module_0

class Test_Dcc_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            date_0 = None
            none_type_0 = None
            decimal_0 = module_0.dcfc_30_e_360(date_0, date_0, date_0, none_type_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
