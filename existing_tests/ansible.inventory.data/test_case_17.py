import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '3S]0I=5c\\yd\\V& cX5'
            dict_0 = {str_0: str_0, str_0: str_0}
            inventory_data_0 = module_0.InventoryData()
            var_0 = inventory_data_0.remove_group(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
