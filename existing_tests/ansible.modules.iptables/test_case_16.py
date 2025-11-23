import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bool_0 = True
            str_0 = '4[g#X{#E{*v'
            tuple_0 = (str_0,)
            list_0 = [bool_0, bool_0]
            var_0 = module_0.append_jump(tuple_0, tuple_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
