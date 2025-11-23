import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            inventory_data_0 = module_0.InventoryData()
            str_0 = 's;'
            var_0 = inventory_data_0.add_host(str_0)
            var_1 = inventory_data_0.reconcile_inventory()
            var_2 = inventory_data_0.add_group(str_0)
            tuple_0 = None
            var_3 = inventory_data_0.remove_group(str_0)
            str_1 = 'p2\x0bg{;V'
            var_4 = inventory_data_0.get_host(str_1)
            var_5 = inventory_data_0.reconcile_inventory()
            inventory_data_1 = module_0.InventoryData()
            str_2 = 'GC/P0jE?'
            float_0 = None
            var_6 = inventory_data_0.add_host(str_2, float_0)
            bytes_0 = b'3R\xc1\xbb<g\xc3'
            var_7 = inventory_data_0.add_host(bytes_0, tuple_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
