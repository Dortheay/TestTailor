import unittest
import timeout_decorator
import ansible.plugins.inventory.advanced_host_list as module_0

class Test_Advanced_host_list_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            inventory_module_1 = module_0.InventoryModule()
            dict_0 = {inventory_module_0: inventory_module_1}
            var_0 = inventory_module_0.verify_file(dict_0)
            tuple_0 = ()
            list_0 = None
            str_0 = ''
            var_1 = inventory_module_0.parse(tuple_0, list_0, str_0)
            tuple_1 = None
            bytes_0 = b'\xef\x8d"N\xc1\xb5Bx\x99A\xdb\x159'
            float_0 = 1990.3
            var_2 = inventory_module_1.parse(tuple_1, bytes_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
