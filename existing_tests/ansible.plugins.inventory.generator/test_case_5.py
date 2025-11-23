import unittest
import timeout_decorator
import ansible.plugins.inventory.generator as module_0

class Test_Generator_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            dict_0 = None
            str_0 = 'Z6QS#g\rsFS*'
            set_0 = {str_0, dict_0, str_0, dict_0}
            inventory_module_0 = module_0.InventoryModule()
            var_0 = inventory_module_0.parse(dict_0, str_0, set_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
