import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        inventory_data_0 = module_0.InventoryData()
        str_0 = 'testhost'
        var_0 = inventory_data_0.add_host(str_0)
        str_1 = 'localhost'
        var_1 = inventory_data_0.add_host(str_1)
        var_2 = inventory_data_0.get_host(str_0)
        var_3 = inventory_data_0.get_host(str_1)
        str_2 = 'nonexistent'
        var_4 = inventory_data_0.get_host(str_2)

if __name__ == "__main__":
    unittest.main()
