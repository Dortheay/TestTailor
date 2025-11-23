import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            bool_0 = False
            str_0 = "q,Rvl,G?;!7>'"
            str_1 = '0\tDC>bd(x&j_p,+N3'
            dict_0 = {}
            set_0 = set()
            str_2 = 'ANSIBALLZ: Using lock for %s'
            tuple_0 = (str_2,)
            inventory_manager_0 = module_0.InventoryManager(set_0, tuple_0)
            var_0 = inventory_manager_0.subset(dict_0)
            list_0 = []
            var_1 = inventory_manager_0.get_hosts(list_0)
            set_1 = {bool_0, str_1}
            inventory_manager_1 = module_0.InventoryManager(bool_0, str_0, set_1)
            var_2 = inventory_manager_1.refresh_inventory()
            str_3 = '/tmp/tmp.h3khK58kUm/Z4&{*{)9XN$[-e \n=w#'
            var_3 = inventory_manager_1.add_host(bool_0, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
