import unittest
import timeout_decorator
import ansible.plugins.inventory.host_list as module_0

class Test_Host_list_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '2Fs\\'
            set_0 = None
            str_1 = ''
            inventory_module_0 = module_0.InventoryModule()
            var_0 = inventory_module_0.parse(str_0, set_0, str_1)
            bytes_0 = None
            str_2 = 'ask_vault_pass'
            float_0 = 512.0
            var_1 = inventory_module_0.parse(float_0, bytes_0, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
