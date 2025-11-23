import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = None
        str_0 = '6'
        list_0 = [int_0, int_0]
        dict_0 = {int_0: int_0}
        bool_0 = False
        var_0 = module_0.append_csv(list_0, bool_0, list_0)
        var_1 = module_0.main()
        list_1 = [list_0, int_0, dict_0]
        set_0 = {int_0, list_0, list_0, list_1}
        bytes_0 = b'\x9ca/\xb7\xd4\xeb\xeb\xe0.W\x01\xf9\xd7\xf1\x84\xd5\x9d\xc4?'
        var_2 = module_0.push_arguments(int_0, bytes_0, set_0)
        bool_1 = True
        var_3 = module_0.set_chain_policy(list_1, str_0, bool_1)

if __name__ == "__main__":
    unittest.main()
