import unittest
import timeout_decorator
import ansible.plugins.inventory.generator as module_0

class Test_Generator_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bool_0 = False
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(bool_0)

if __name__ == "__main__":
    unittest.main()
