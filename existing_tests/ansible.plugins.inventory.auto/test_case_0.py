import unittest
import timeout_decorator
import ansible.plugins.inventory.auto as module_0

class Test_Auto_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            inventory_module_1 = module_0.InventoryModule()
            var_0 = inventory_module_1.verify_file(inventory_module_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
