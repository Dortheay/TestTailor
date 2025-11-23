import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            dict_0 = {}
            list_0 = [dict_0]
            bytes_0 = b'\x02\x88\xaf'
            float_0 = -119.541
            var_0 = module_0.append_match_flag(dict_0, list_0, bytes_0, float_0)
            bytes_1 = b'\x9ep\x05C%|\xc8\xeaC4'
            tuple_0 = None
            int_0 = -3381
            tuple_1 = (tuple_0, int_0)
            dict_1 = {}
            var_1 = module_0.set_chain_policy(bytes_1, tuple_1, dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
