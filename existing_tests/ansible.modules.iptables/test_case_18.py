import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'ansible.modules.iptables'
            list_0 = [str_0]
            tuple_0 = None
            var_0 = module_0.remove_rule(list_0, list_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
