import unittest
import timeout_decorator
import pypara.dcc as module_0

class Test_Dcc_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            date_0 = None
            str_0 = 'bRQ]E[F.LN#~G!<<'
            callable_0 = module_0.dcc(str_0)
            decimal_0 = module_0.dcfc_act_360(date_0, date_0, date_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
