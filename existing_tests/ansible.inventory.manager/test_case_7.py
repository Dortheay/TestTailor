import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '&intersect_this'
            str_1 = 'regular_pattern'
            var_0 = None
            str_2 = ''
            int_0 = 1682
            list_0 = [str_1, int_0, str_0, int_0]
            inventory_manager_0 = module_0.InventoryManager(list_0)
            str_3 = 'fi?,n^i|z(mYD1<GoRa}'
            tuple_0 = (str_2, str_3)
            inventory_manager_1 = module_0.InventoryManager(inventory_manager_0, tuple_0)
            list_1 = [var_0]
            bytes_0 = b'e\x94\xf0\x06$}{\x04\xaaz\x1b'
            inventory_manager_2 = module_0.InventoryManager(list_1, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
