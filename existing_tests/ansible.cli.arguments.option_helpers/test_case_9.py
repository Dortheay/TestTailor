import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = '921'
            dict_0 = {str_0: str_0, str_0: str_0}
            str_1 = '&jm<3y'
            set_0 = set()
            prepend_list_action_0 = module_0.PrependListAction(dict_0, str_1, set_0)
            int_0 = 1298
            sorting_help_formatter_0 = module_0.SortingHelpFormatter(int_0)
            var_0 = module_0.add_async_options(sorting_help_formatter_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
