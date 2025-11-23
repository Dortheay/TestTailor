import unittest
import timeout_decorator
import ansible.plugins.action.include_vars as module_0

class Test_Include_vars_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = None
            int_0 = 1205
            dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: int_0, bytes_0: bytes_0}
            int_1 = -1361
            bool_0 = None
            bytes_1 = None
            set_0 = {bool_0, bytes_1}
            str_0 = '\rB'
            list_0 = [bytes_0]
            bool_1 = False
            tuple_0 = (bool_1, list_0)
            action_module_0 = module_0.ActionModule(dict_0, list_0, int_0, tuple_0, bytes_1, tuple_0)
            int_2 = 3
            bytes_2 = b'\xad\x7f\x01\xa7'
            str_1 = '0^<!ZcFbm{7'
            action_module_1 = module_0.ActionModule(set_0, str_0, action_module_0, int_2, bytes_2, str_1)
            bool_2 = None
            action_module_2 = module_0.ActionModule(bytes_1, action_module_1, str_0, tuple_0, bool_2, str_0)
            str_2 = "-vb~`Y8NmL66V'>\tVc"
            tuple_1 = (action_module_2, bytes_0, str_2, list_0)
            tuple_2 = (int_1, bool_0, tuple_1)
            action_module_3 = module_0.ActionModule(bytes_0, dict_0, tuple_2, action_module_2, action_module_0, set_0)
            str_3 = ''
            bool_3 = True
            bool_4 = False
            bool_5 = True
            int_3 = 2751
            bool_6 = None
            tuple_3 = (bool_6,)
            bool_7 = True
            bytes_3 = b'\x7f\xedP\xc9\xb8\xab\x80@_\xdb\x91+\xc3\x85\xdd\x1d\xc6'
            action_module_4 = module_0.ActionModule(bool_3, bool_5, int_3, tuple_3, bool_7, bytes_3)
            str_4 = 'gY"yGS!iW4SJ_*i'
            list_1 = []
            action_module_5 = module_0.ActionModule(action_module_4, str_4, bytes_3, action_module_4, list_1, str_4)
            float_0 = 55.4787
            set_1 = None
            tuple_4 = (action_module_5, float_0, set_1, str_4)
            action_module_6 = module_0.ActionModule(bool_3, bool_4, action_module_5, tuple_4, bytes_3, tuple_4)
            var_0 = action_module_6.run(action_module_3, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
