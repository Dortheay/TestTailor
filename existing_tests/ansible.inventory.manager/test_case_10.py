import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            set_0 = set()
            str_0 = ''
            inventory_manager_0 = module_0.InventoryManager(set_0, str_0)
            var_0 = inventory_manager_0.clear_pattern_cache()
            var_1 = inventory_manager_0.list_groups()
            str_1 = 'w<H.=Cm[f/xhJ8 f-$`N'
            var_2 = inventory_manager_0.remove_restriction()
            str_2 = 'JK e'
            tuple_0 = (str_1, str_2)
            int_0 = 722
            str_3 = ' f%Ady"7\'5z9\''
            var_3 = inventory_manager_0.list_groups()
            var_4 = inventory_manager_0.parse_sources(int_0)
            var_5 = inventory_manager_0.clear_pattern_cache()
            var_6 = inventory_manager_0.add_group(str_3)
            str_4 = ''
            list_0 = [inventory_manager_0, var_1, str_1]
            var_7 = inventory_manager_0.subset(list_0)
            str_5 = '^model name.*UML'
            list_1 = []
            inventory_manager_1 = module_0.InventoryManager(str_1, list_1)
            var_8 = inventory_manager_1.get_host(str_5)
            var_9 = module_0.split_host_pattern(str_4)
            float_0 = 718.437
            var_10 = inventory_manager_0.list_hosts()
            inventory_manager_2 = module_0.InventoryManager(tuple_0, int_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
