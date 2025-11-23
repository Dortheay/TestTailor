import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = '2d^AX,'
            bool_0 = False
            tuple_0 = ()
            var_0 = module_0.append_match_flag(str_0, bool_0, str_0, tuple_0)
            list_0 = None
            str_1 = 'import \\w+'
            str_2 = "%&ToxT1V'0sq"
            var_1 = module_0.append_wait(list_0, str_1, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
