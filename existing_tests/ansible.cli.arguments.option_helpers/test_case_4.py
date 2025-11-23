import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 3027
            list_0 = [int_0, int_0, int_0, int_0]
            float_0 = 99.225
            unrecognized_argument_0 = module_0.UnrecognizedArgument(list_0, int_0, float_0)
            int_1 = 1011
            bool_0 = True
            str_0 = '+Si, PW<h/;bUy%m'
            prepend_list_action_0 = module_0.PrependListAction(bool_0, str_0, int_1, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
