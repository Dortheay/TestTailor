import unittest
import timeout_decorator
import ansible.plugins.action.validate_argument_spec as module_0

class Test_Validate_argument_spec_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -1701
            dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
            list_0 = [dict_0, int_0, int_0, dict_0]
            float_0 = 2520.6
            float_1 = 509.26444
            set_0 = {float_1}
            int_1 = 1716
            bytes_0 = b'4\xe7j\xa2\xdce'
            list_1 = [int_1]
            action_module_0 = module_0.ActionModule(float_1, set_0, int_1, bytes_0, list_1, bytes_0)
            var_0 = action_module_0.get_args_from_task_vars(list_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
