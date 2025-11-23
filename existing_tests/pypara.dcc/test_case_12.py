import unittest
import timeout_decorator
import pypara.dcc as module_0

class Test_Dcc_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()

if __name__ == "__main__":
    unittest.main()
