import unittest
import timeout_decorator
import ansible.plugins.action.debug as module_0

class Test_Debug_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '-N~4\tO_iNk|Op'
            set_0 = None
            tuple_0 = (str_0, set_0)
            str_1 = '7_\ruN\nP'
            str_2 = 'Z"uc:'
            bool_0 = True
            set_1 = {str_0, str_2, tuple_0}
            int_0 = -433
            bool_1 = True
            str_3 = '^|6%?w'
            list_0 = []
            list_1 = [str_1, str_0, list_0, str_0]
            int_1 = -1231
            int_2 = -870
            str_4 = '1fV'
            float_0 = 254.218418
            bytes_0 = b'\xeb\xc6t\xe6-+l\xca\xa5\xc2a\x15WT@`L\x9e'
            tuple_1 = (bytes_0,)
            dict_0 = {tuple_1: int_2}
            action_module_0 = module_0.ActionModule(int_1, int_2, set_0, str_4, float_0, dict_0)
            int_3 = -1608
            bytes_1 = b'\xb4\xde\xc5$\xe5\xaa^y#~'
            float_1 = 2237.76538
            action_module_1 = module_0.ActionModule(action_module_0, int_3, bool_0, bytes_1, set_0, float_1)
            str_5 = 'p86elO9e;M2\t4'
            action_module_2 = module_0.ActionModule(bool_1, str_3, list_1, action_module_1, float_0, str_5)
            var_0 = action_module_2.run(set_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
