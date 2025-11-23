import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'w<H.=Cm[f/xhJ8 f-$`N'
            str_1 = 'JK e'
            tuple_0 = (str_0, str_1)
            str_2 = ''
            str_3 = '^model name.*UML'
            str_4 = 'QXt,ve;D~XC,\t'
            list_0 = []
            inventory_manager_0 = module_0.InventoryManager(str_4, list_0)
            var_0 = inventory_manager_0.get_host(str_3)
            var_1 = module_0.split_host_pattern(str_2)
            var_2 = inventory_manager_0.restrict_to_hosts(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
