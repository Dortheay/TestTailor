import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        str_0 = 'test_host'
        host_0 = module_0.Host(str_0)
        str_1 = 'ansible_port'
        int_0 = 22
        var_0 = host_0.set_variable(str_1, int_0)
        str_2 = 'nested_dict'
        str_3 = 'key1'
        str_4 = 'value1'
        str_5 = {str_3: str_4}
        var_1 = host_0.set_variable(str_2, str_5)
        str_6 = 'key2'
        str_7 = 'value2'
        str_8 = {str_6: str_7}
        var_2 = host_0.set_variable(str_2, str_8)

if __name__ == "__main__":
    unittest.main()
