import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            unrecognized_argument_0 = None
            int_0 = -330
            float_0 = -69.6786
            sorting_help_formatter_0 = module_0.SortingHelpFormatter(unrecognized_argument_0, int_0, float_0)
            ansible_version_0 = module_0.AnsibleVersion(unrecognized_argument_0, sorting_help_formatter_0)
            float_1 = 512.0
            str_0 = "XOMy\nvWD-I'%TB"
            tuple_0 = (ansible_version_0, float_1, unrecognized_argument_0, str_0)
            float_2 = 0.0
            int_1 = 1632
            sorting_help_formatter_1 = module_0.SortingHelpFormatter(float_2, int_1)
            var_0 = sorting_help_formatter_1.add_arguments(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
