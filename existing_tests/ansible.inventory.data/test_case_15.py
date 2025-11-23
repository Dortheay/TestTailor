import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            tuple_0 = ()
            inventory_data_0 = module_0.InventoryData()
            var_0 = inventory_data_0.add_group(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
