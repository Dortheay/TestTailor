import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            var_0 = module_0.version()
            bytes_0 = b'\x02:\xb9\xeeW^\xe1\xf6\x06\x07\xf0'
            tuple_0 = ()
            set_0 = None
            ansible_version_0 = None
            sorting_help_formatter_0 = module_0.SortingHelpFormatter(ansible_version_0)
            bytes_1 = b'?\x07\n\xa3^\xdcB\xa3#3n\x84s\x87}42J\x17 '
            prepend_list_action_0 = module_0.PrependListAction(tuple_0, set_0, bytes_1)
            prepend_list_action_1 = module_0.PrependListAction(bytes_0, prepend_list_action_0)
            float_0 = 772.03342
            var_1 = sorting_help_formatter_0.add_arguments(tuple_0)
            var_2 = module_0.create_base_parser(float_0, set_0, float_0)
            bytes_2 = b'DX}\x93N\x93\x1bc'
            str_0 = 'd'
            float_1 = -66.98441938319507
            prepend_list_action_2 = module_0.PrependListAction(bytes_2, prepend_list_action_1, str_0, bytes_0, float_1, prepend_list_action_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
