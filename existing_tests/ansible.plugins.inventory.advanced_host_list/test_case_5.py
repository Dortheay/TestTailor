import unittest
import timeout_decorator
import ansible.plugins.inventory.advanced_host_list as module_0

class Test_Advanced_host_list_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            int_0 = 1359
            bytes_0 = None
            str_0 = 'x#h$f<JvP.fMX_e!d(['
            var_0 = inventory_module_0.parse(int_0, bytes_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
