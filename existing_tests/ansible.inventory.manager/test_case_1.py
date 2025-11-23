import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'D'
            int_0 = 1950
            inventory_manager_0 = None
            tuple_0 = (int_0, str_0, inventory_manager_0)
            tuple_1 = (tuple_0,)
            str_1 = 'z@XA$ V'
            dict_0 = {str_0: tuple_1, str_1: int_0, str_0: str_1}
            inventory_manager_1 = module_0.InventoryManager(str_0, dict_0)
            var_0 = module_0.split_host_pattern(tuple_0)
            list_0 = [inventory_manager_0, dict_0]
            var_1 = inventory_manager_0.get_host(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
