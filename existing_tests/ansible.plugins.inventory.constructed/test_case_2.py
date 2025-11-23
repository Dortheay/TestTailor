import unittest
import timeout_decorator
import ansible.plugins.inventory.constructed as module_0

class Test_Constructed_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            list_0 = [inventory_module_0, inventory_module_0]
            str_0 = 'lL(Oc8:@C[96c;Ft[Z'
            set_0 = {str_0}
            var_0 = inventory_module_0.parse(list_0, str_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
