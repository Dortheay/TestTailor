import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'test_host'
        var_0 = inventory_data_0.add_host(str_0)
        var_1 = inventory_data_0.get_host(str_0)
        group_0 = module_1.Group()
        var_2 = inventory_data_0.remove_host(group_0)

if __name__ == "__main__":
    unittest.main()
