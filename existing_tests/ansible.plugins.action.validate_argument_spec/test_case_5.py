import unittest
import timeout_decorator
import ansible.plugins.action.validate_argument_spec as module_0

class Test_Validate_argument_spec_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = 4849
            str_0 = 'woJ?UJwbpy0'
            bool_0 = True
            float_0 = -3541.97
            dict_0 = {bool_0: float_0, int_0: bool_0, str_0: str_0, bool_0: str_0}
            str_1 = 'VWGj\t-Y'
            bytes_0 = b'\xc4\xf0/x\x97\xd8\x97\xbe\xecy/\xeb\x9b\xfd\x08\x9e\xae^)\xde'
            tuple_0 = (str_1,)
            list_0 = [str_1, str_1]
            bytes_1 = b'\x91\xd0\x93\x109\x00r\x8d\xa4\x9a\xed'
            action_module_0 = module_0.ActionModule(str_1, str_1, bytes_0, tuple_0, list_0, bytes_1)
            var_0 = action_module_0.get_args_from_task_vars(dict_0, bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
