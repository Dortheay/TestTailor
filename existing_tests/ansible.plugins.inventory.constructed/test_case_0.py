import unittest
import timeout_decorator
import ansible.plugins.inventory.constructed as module_0

class Test_Constructed_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = []
            float_0 = 340.654
            inventory_module_0 = module_0.InventoryModule()
            var_0 = inventory_module_0.get_all_host_vars(list_0, float_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
