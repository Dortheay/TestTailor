import unittest
import timeout_decorator
import ansible.plugins.action.wait_for_connection as module_0

class Test_Wait_for_connection_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -262
            set_0 = {int_0}
            str_0 = ';!'
            bool_0 = True
            str_1 = None
            dict_0 = {str_0: bool_0, str_1: bool_0}
            int_1 = 8192
            bytes_0 = b'\xce\xdd\xab\x96\x8cb\xfb\xc7\x016\x98\x9f'
            set_1 = {int_1}
            str_2 = '2KMHZqP5%`\tlc'
            list_0 = [int_1]
            tuple_0 = (str_2, list_0)
            int_2 = 856
            str_3 = 'dlEr61iZ=E%tBOc7'
            str_4 = 'u3,Q0%zx0V['
            action_module_0 = module_0.ActionModule(set_1, tuple_0, int_2, str_3, set_1, str_4)
            bool_1 = False
            action_module_1 = module_0.ActionModule(int_1, bytes_0, action_module_0, bool_1, list_0, bool_1)
            var_0 = action_module_1.do_until_success_or_timeout(set_0, int_0, dict_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
