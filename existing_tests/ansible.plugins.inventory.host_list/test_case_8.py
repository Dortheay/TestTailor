import unittest
import timeout_decorator
import ansible.plugins.inventory.host_list as module_0

class Test_Host_list_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            str_0 = '2Fsy'
            set_0 = None
            str_1 = ''
            inventory_module_1 = module_0.InventoryModule()
            var_0 = inventory_module_1.parse(str_0, set_0, str_1)
            inventory_module_2 = module_0.InventoryModule()
            str_2 = 'ask_vault_pass'
            inventory_module_3 = module_0.InventoryModule()
            inventory_module_4 = module_0.InventoryModule()
            var_1 = inventory_module_4.verify_file(str_2)
            float_0 = 512.0
            list_0 = [float_0]
            int_0 = None
            var_2 = inventory_module_2.verify_file(list_0)
            str_3 = '/etc'
            var_3 = inventory_module_2.verify_file(str_3)
            bytes_0 = b'\xc2\xcfw'
            var_4 = inventory_module_2.parse(list_0, int_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
