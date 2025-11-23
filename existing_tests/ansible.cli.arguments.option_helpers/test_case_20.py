import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            tuple_0 = ()
            float_0 = -599.0
            var_0 = module_0.version(float_0)
            str_0 = "'1I\ra#S"
            set_0 = None
            bytes_0 = b'?\x07\n\xa3^\xdcB\xa3#3n\x84s\x87}42J\x17 '
            prepend_list_action_0 = module_0.PrependListAction(tuple_0, set_0, bytes_0)
            prepend_list_action_1 = module_0.PrependListAction(str_0, set_0)
            str_1 = '&~0^IQeua/3'
            var_1 = module_0.ensure_value(set_0, str_1, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
