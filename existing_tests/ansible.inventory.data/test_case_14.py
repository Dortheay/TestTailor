import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = None
            inventory_data_0 = module_0.InventoryData()
            dict_0 = {inventory_data_0: list_0}
            var_0 = inventory_data_0.add_group(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
