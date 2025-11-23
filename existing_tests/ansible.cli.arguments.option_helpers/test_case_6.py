import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            var_0 = module_0.unfrack_path()
            list_0 = []
            sorting_help_formatter_0 = module_0.SortingHelpFormatter(list_0)
            float_0 = 952.47607
            tuple_0 = (sorting_help_formatter_0, float_0)
            var_1 = module_0.add_basedir_options(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
