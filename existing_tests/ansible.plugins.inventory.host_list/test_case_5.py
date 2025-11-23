import unittest
import timeout_decorator
import ansible.plugins.inventory.host_list as module_0

class Test_Host_list_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            float_0 = -710.5
            int_0 = None
            str_0 = '4W,sDBI'
            var_0 = inventory_module_0.parse(float_0, int_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
