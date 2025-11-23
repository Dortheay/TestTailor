import unittest
import timeout_decorator
import pypara.dcc as module_0

class Test_Dcc_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = 'Q+nlTu@)\nlp3xH^[R'
            d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
            optional_0 = d_c_c_registry_machinery_0.find(str_0)
            date_0 = None
            decimal_0 = module_0.dcfc_30_e_plus_360(date_0, date_0, date_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
