import unittest
import timeout_decorator
import ansible.plugins.inventory.constructed as module_0

class Test_Constructed_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            set_0 = set()
            int_0 = None
            list_0 = []
            inventory_module_1 = None
            var_0 = inventory_module_0.parse(int_0, list_0, inventory_module_1, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
