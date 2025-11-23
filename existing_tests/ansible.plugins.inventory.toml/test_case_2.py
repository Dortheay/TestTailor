import unittest
import timeout_decorator
import ansible.plugins.inventory.toml as module_0

class Test_Toml_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            list_0 = None
            bool_0 = False
            str_0 = 'RT'
            inventory_module_0 = module_0.InventoryModule()
            var_0 = inventory_module_0.parse(list_0, bool_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
