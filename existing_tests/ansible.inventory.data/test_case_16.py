import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'A-'
            inventory_data_0 = module_0.InventoryData()
            var_0 = inventory_data_0.remove_group(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
