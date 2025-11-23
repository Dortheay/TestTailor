import unittest
import timeout_decorator
import pypara.dcc as module_0

class Test_Dcc_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '7xj2"LZ(xbSbeJh#V'
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        optional_0 = d_c_c_registry_machinery_0.find(str_0)

if __name__ == "__main__":
    unittest.main()
