import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        str_0 = 'test_host'
        host_0 = module_0.Host(str_0)
        str_1 = 'test_group'
        group_0 = module_1.Group(str_1)
        var_0 = host_0.add_group(group_0)
        host_1 = module_0.Host()

if __name__ == "__main__":
    unittest.main()
