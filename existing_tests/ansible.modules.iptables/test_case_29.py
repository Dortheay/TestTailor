import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            int_0 = None
            float_0 = -16.677540020905248
            str_0 = ''
            float_1 = -543.7252148541515
            dict_0 = {str_0: float_0, int_0: float_1}
            var_0 = module_0.append_match_flag(float_0, str_0, str_0, dict_0)
            str_1 = 'wUtYc'
            bool_0 = True
            list_0 = [bool_0, dict_0, float_0, float_0]
            var_1 = module_0.append_param(str_1, str_0, bool_0, list_0)
            str_2 = 'l&1?W;N:b{w#"REW'
            set_0 = None
            var_2 = module_0.append_wait(str_2, set_0, int_0)
            tuple_0 = ()
            str_3 = '22'
            var_3 = module_0.push_arguments(float_1, set_0, tuple_0, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
