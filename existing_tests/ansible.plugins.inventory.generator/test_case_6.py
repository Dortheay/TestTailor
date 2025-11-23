import unittest
import timeout_decorator
import ansible.plugins.inventory.generator as module_0

class Test_Generator_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = -1559
            inventory_module_0 = module_0.InventoryModule()
            tuple_0 = ()
            complex_0 = None
            set_0 = {tuple_0, int_0, inventory_module_0}
            var_0 = inventory_module_0.parse(tuple_0, tuple_0, complex_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
