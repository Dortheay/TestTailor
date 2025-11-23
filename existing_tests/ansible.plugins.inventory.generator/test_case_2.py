import unittest
import timeout_decorator
import ansible.plugins.inventory.generator as module_0

class Test_Generator_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -1873.0
            str_0 = '6QR\\S|"<13(MuC'
            inventory_module_0 = module_0.InventoryModule()
            var_0 = inventory_module_0.template(float_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
