import unittest
import timeout_decorator
import ansible.plugins.inventory.host_list as module_0

class Test_Host_list_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            dict_0 = {}
            int_0 = 2710
            var_0 = inventory_module_0.parse(dict_0, dict_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
