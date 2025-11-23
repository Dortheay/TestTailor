import unittest
import timeout_decorator
import ansible.plugins.action.fail as module_0

class Test_Fail_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'Buffers'
            dict_0 = {}
            bytes_0 = b''
            bool_0 = True
            tuple_0 = None
            complex_0 = None
            float_0 = 512.0
            set_0 = {bool_0, tuple_0}
            action_module_0 = module_0.ActionModule(complex_0, str_0, tuple_0, tuple_0, float_0, set_0)
            str_1 = 'dl`ka2U&a#I9'
            action_module_1 = module_0.ActionModule(bytes_0, dict_0, bool_0, tuple_0, str_1, dict_0)
            int_0 = -2224
            float_1 = -320.534
            var_0 = action_module_1.run(int_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
