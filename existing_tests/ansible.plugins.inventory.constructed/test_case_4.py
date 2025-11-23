import unittest
import timeout_decorator
import ansible.plugins.inventory.constructed as module_0

class Test_Constructed_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        inventory_module_0 = module_0.InventoryModule()

if __name__ == "__main__":
    unittest.main()
