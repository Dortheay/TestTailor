import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '3S]0I=5c\\yd\\V& cX5'
            str_1 = 'f#%&'
            float_0 = -839.7
            inventory_data_0 = module_0.InventoryData()
            var_0 = inventory_data_0.set_variable(str_0, str_1, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
