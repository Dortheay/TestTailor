import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        str_0 = 'name'
        str_1 = 'test_group'
        str_2 = {str_0: str_1}
        str_3 = 'vars'
        str_4 = 'address'
        str_5 = 'uuid'
        str_6 = 'implicit'
        str_7 = 'groups'
        str_8 = 'test_host'
        str_9 = 'ansible_port'
        int_0 = 22
        int_1 = {str_9: int_0}
        str_10 = '192.168.1.1'
        str_11 = 'test-uuid'
        bool_0 = True
        str_12 = [str_2]
        var_0 = {str_0: str_8, str_3: int_1, str_4: str_10, str_5: str_11, str_6: bool_0, str_7: str_12}
        host_0 = module_0.Host()
        var_1 = host_0.deserialize(var_0)
        var_2 = host_0.groups
        var_3 = len(var_2)

if __name__ == "__main__":
    unittest.main()
