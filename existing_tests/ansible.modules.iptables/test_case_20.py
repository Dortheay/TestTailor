import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = 'ITx`l9{k'
            bool_0 = True
            str_1 = '*'
            var_0 = module_0.append_rule(str_0, bool_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
