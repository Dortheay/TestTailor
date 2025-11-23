import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        int_0 = 5564
        int_1 = 357
        inventory_manager_0 = module_0.InventoryManager(int_1)
        dict_0 = None
        tuple_0 = (dict_0,)
        var_0 = inventory_manager_0.get_host(tuple_0)
        float_0 = 537.64
        bytes_0 = b'\x8a\x0b\x15\xf1_.Y\xa3\x89'
        var_1 = inventory_manager_0.clear_caches()
        tuple_1 = (int_0, float_0, bytes_0)
        dict_1 = {}
        inventory_manager_1 = module_0.InventoryManager(tuple_1, int_0, dict_1)
        var_2 = inventory_manager_1.clear_caches()

if __name__ == "__main__":
    unittest.main()
