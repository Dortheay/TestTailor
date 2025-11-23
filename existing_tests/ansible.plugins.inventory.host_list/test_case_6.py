import unittest
import timeout_decorator
import ansible.plugins.inventory.host_list as module_0

class Test_Host_list_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            str_0 = '),4a-n<'
            inventory_module_1 = module_0.InventoryModule()
            float_0 = 2.0
            var_0 = inventory_module_0.verify_file(str_0)
            inventory_module_2 = module_0.InventoryModule()
            var_1 = inventory_module_1.verify_file(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
