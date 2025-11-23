import unittest
import timeout_decorator
import pypara.dcc as module_0

class Test_Dcc_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
            date_0 = None
            decimal_0 = module_0.dcfc_nl_365(date_0, date_0, date_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
