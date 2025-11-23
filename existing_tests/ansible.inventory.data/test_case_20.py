import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            inventory_data_0 = module_0.InventoryData()
            str_0 = 'test_host'
            var_0 = inventory_data_0.add_host(str_0)
            str_1 = 'test_group'
            var_1 = inventory_data_0.add_group(str_1)
            var_2 = inventory_data_0.add_host(str_0, str_1)
            var_3 = inventory_data_0.groups[str_1]
            var_4 = None
            var_5 = inventory_data_0.add_host(var_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
