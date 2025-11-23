import unittest
import timeout_decorator
import ansible.plugins.inventory.yaml as module_0

class Test_Yaml_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = {}
            inventory_module_0 = module_0.InventoryModule()
            str_0 = 'R'
            bytes_0 = b'\x96\xfb-\x8b\x00r'
            var_0 = inventory_module_0.verify_file(bytes_0)
            inventory_module_1 = module_0.InventoryModule()
            var_1 = inventory_module_1.parse(bytes_0, dict_0, inventory_module_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
