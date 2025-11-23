import unittest
import timeout_decorator
import ansible.plugins.inventory.host_list as module_0

class Test_Host_list_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = None
            inventory_module_0 = module_0.InventoryModule()
            float_0 = 512.0
            str_0 = '0_B4IsC;R}['
            var_0 = inventory_module_0.parse(float_0, bytes_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
