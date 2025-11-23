import unittest
import timeout_decorator
import ansible.plugins.inventory.generator as module_0

class Test_Generator_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -285
            inventory_module_0 = module_0.InventoryModule()
            list_0 = [int_0, int_0, inventory_module_0, inventory_module_0]
            tuple_0 = (int_0, int_0, list_0)
            dict_0 = {}
            inventory_module_1 = module_0.InventoryModule()
            var_0 = inventory_module_1.add_parents(tuple_0, inventory_module_0, inventory_module_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
