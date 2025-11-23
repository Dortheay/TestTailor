import unittest
import timeout_decorator
import ansible.plugins.inventory.yaml as module_0

class Test_Yaml_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = -1458
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(int_0)

if __name__ == "__main__":
    unittest.main()
