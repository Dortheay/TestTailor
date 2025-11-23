import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        str_0 = 'test_host'
        host_0 = module_0.Host(str_0)
        str_1 = 'test_group'
        group_0 = module_1.Group(str_1)
        var_0 = host_0.add_group(group_0)
        var_1 = host_0.get_groups()
        var_2 = host_0.add_group(group_0)
        var_3 = host_0.get_groups()
        str_2 = 'ancestor_group'
        group_1 = module_1.Group(str_2)
        var_4 = host_0.add_group(group_0)
        var_5 = host_0.get_groups()

if __name__ == "__main__":
    unittest.main()
