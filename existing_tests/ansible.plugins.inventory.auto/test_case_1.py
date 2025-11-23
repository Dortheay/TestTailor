import unittest
import timeout_decorator
import ansible.plugins.inventory.auto as module_0

class Test_Auto_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = None
            str_0 = "rJMo_:'("
            tuple_0 = (str_0,)
            set_0 = None
            tuple_1 = (tuple_0, set_0, set_0)
            inventory_module_0 = module_0.InventoryModule()
            var_0 = inventory_module_0.parse(bool_0, str_0, tuple_1, tuple_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
