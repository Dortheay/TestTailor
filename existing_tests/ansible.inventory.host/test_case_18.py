import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'test_host'
        host_0 = module_0.Host(str_0)
        group_0 = module_1.Group(str_0)
        group_1 = module_1.Group(str_0)
        var_0 = host_0.add_group(group_0)
        var_1 = host_0.get_groups()
        var_2 = host_0.remove_group(group_0)
        var_3 = host_0.get_magic_vars()

if __name__ == "__main__":
    unittest.main()
