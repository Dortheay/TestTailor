import unittest
import timeout_decorator
import ansible.plugins.inventory.auto as module_0

class Test_Auto_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        inventory_module_0 = module_0.InventoryModule()
        str_0 = 'inventory.yml'
        var_0 = inventory_module_0.verify_file(str_0)
        str_1 = 'inventory.yaml'
        var_1 = inventory_module_0.verify_file(str_1)

if __name__ == "__main__":
    unittest.main()
