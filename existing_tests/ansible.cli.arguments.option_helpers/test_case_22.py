import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            var_0 = module_0.version()
            bytes_0 = b'\x02:\xb9\xeeW^\xe1\xf6\x06\x07\xf0'
            tuple_0 = ()
            str_0 = '5!Oj.Y`2XL~=LqMMX?_'
            str_1 = "'1I\ra#S"
            list_0 = [str_0, str_1, tuple_0]
            bool_0 = False
            var_1 = module_0.unfrack_path()
            str_2 = 'LoVP5'
            float_0 = -152.81843
            unrecognized_argument_0 = module_0.UnrecognizedArgument(str_1, bool_0, str_2, float_0)
            set_0 = None
            ansible_version_0 = None
            ansible_version_1 = None
            sorting_help_formatter_0 = module_0.SortingHelpFormatter(ansible_version_1)
            ansible_version_2 = module_0.AnsibleVersion(list_0, set_0, ansible_version_0, sorting_help_formatter_0)
            dict_0 = None
            bool_1 = False
            str_3 = '\n_raw:\n  description:\n    - a password\n  type: list\n  elements: str\n'
            int_0 = -3760
            unrecognized_argument_1 = module_0.UnrecognizedArgument(str_1, bool_1, str_3, sorting_help_formatter_0, dict_0, int_0)
            sorting_help_formatter_1 = None
            unrecognized_argument_2 = module_0.UnrecognizedArgument(unrecognized_argument_1, set_0, sorting_help_formatter_1, bytes_0)
            bool_2 = None
            int_1 = -1894
            tuple_1 = (int_1,)
            prepend_list_action_0 = module_0.PrependListAction(list_0, unrecognized_argument_2, float_0)
            var_2 = prepend_list_action_0.__call__(bool_2, tuple_1, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
