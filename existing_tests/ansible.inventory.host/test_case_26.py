import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        str_0 = 'test_host'
        host_0 = module_0.Host(str_0)
        str_1 = 'group1'
        group_0 = module_1.Group(str_1)
        str_2 = 'group2'
        group_1 = module_1.Group(str_2)
        str_3 = 'all'
        group_2 = module_1.Group(str_3)
        var_0 = host_0.add_group(group_0)
        var_1 = host_0.get_groups()
        var_2 = host_0.get_groups()
        var_3 = host_0.__getstate__()
        var_4 = host_0.get_groups()
        var_5 = host_0.get_groups()
        float_0 = 0.1
        tuple_0 = ()
        dict_0 = {}
        host_1 = module_0.Host(tuple_0, dict_0)
        var_6 = host_1.remove_group(float_0)
        var_7 = host_0.get_groups()
        var_8 = host_0.get_groups()
        var_9 = host_0.get_groups()

if __name__ == "__main__":
    unittest.main()
