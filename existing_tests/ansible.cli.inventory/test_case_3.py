import unittest
import timeout_decorator
import ansible.cli.inventory as module_0

class Test_Inventory_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'S3x7t<$F3C'
            list_0 = [str_0, str_0]
            inventory_c_l_i_0 = module_0.InventoryCLI(list_0)
            var_0 = inventory_c_l_i_0.inventory_graph()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
