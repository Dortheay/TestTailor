import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            var_0 = module_0.version()
            tuple_0 = ()
            str_0 = '5!Oj.Y`2XL~=LqMMX?_'
            str_1 = "'1I\ra#S"
            list_0 = [str_0, str_1, tuple_0]
            str_2 = '\n        Returns the role name (either the role: or name: field) from\n        the role definition, or (when the role definition is a simple\n        string), just that string\n        '
            int_0 = 0
            set_0 = None
            prepend_list_action_0 = module_0.PrependListAction(list_0, str_2, int_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
