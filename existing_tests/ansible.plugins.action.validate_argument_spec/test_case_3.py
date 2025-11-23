import unittest
import timeout_decorator
import ansible.plugins.action.validate_argument_spec as module_0

class Test_Validate_argument_spec_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b'N\x12\x9f\x8a\xd5\xd3\xe2\xb4\x12\xaf\xf0'
            str_0 = '$3'
            int_0 = 926
            dict_0 = {int_0: int_0}
            bool_0 = True
            int_1 = 1740
            list_0 = [int_1, int_1, bool_0]
            tuple_0 = (bool_0, int_1, list_0, str_0)
            float_0 = 60.0
            action_module_0 = module_0.ActionModule(str_0, int_0, dict_0, tuple_0, dict_0, float_0)
            bool_1 = True
            dict_1 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bool_1: bytes_0}
            bool_2 = True
            str_1 = 'Ewe'
            str_2 = 'M?>qDj\tiC\r}^'
            str_3 = '`gpV1MSQd{^(`hNl\x0c<'
            action_module_1 = None
            list_1 = [action_module_1]
            action_module_2 = module_0.ActionModule(str_1, bool_2, str_2, str_3, dict_1, list_1)
            set_0 = {bool_2, bytes_0}
            var_0 = action_module_2.run(set_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
