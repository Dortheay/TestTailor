import unittest
import timeout_decorator
import ansible.plugins.inventory.auto as module_0

class Test_Auto_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = ')H{'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(str_0)

if __name__ == "__main__":
    unittest.main()
