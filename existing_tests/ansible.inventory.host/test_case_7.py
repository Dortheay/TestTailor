import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'test_host'
            host_0 = module_0.Host(str_0)
            str_1 = "wNKj57'&h+]!F-i"
            group_0 = module_1.Group(str_0)
            str_2 = 'all'
            group_1 = module_1.Group(str_2)
            var_0 = host_0.add_group(group_1)
            var_1 = host_0.get_groups()
            var_2 = host_0.get_groups()
            var_3 = host_0.get_magic_vars()
            int_0 = 9
            int_1 = 695
            dict_0 = {int_0: str_1, host_0: var_1, int_1: int_1, host_0: str_0}
            host_1 = module_0.Host(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
