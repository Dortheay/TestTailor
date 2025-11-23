import unittest
import timeout_decorator
import ansible.plugins.action.validate_argument_spec as module_0

class Test_Validate_argument_spec_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 4849
            str_0 = 'oJ?UJwbpy0'
            bool_0 = True
            float_0 = 1.0
            dict_0 = {bool_0: float_0, int_0: bool_0, str_0: str_0, bool_0: str_0}
            str_1 = ';edY:B+w[mw2\n$e`'
            tuple_0 = (dict_0, float_0, str_1)
            bytes_0 = b'\xb4!\xfa\xea\xa5'
            str_2 = 'VWGj\t-Y'
            list_0 = [str_1, str_1]
            bytes_1 = b'\x91\xd0\x93\x109\x00r\x8d\xa4\x9a\xed'
            action_module_0 = module_0.ActionModule(str_2, str_2, bytes_0, tuple_0, list_0, bytes_1)
            var_0 = action_module_0.get_args_from_task_vars(dict_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
