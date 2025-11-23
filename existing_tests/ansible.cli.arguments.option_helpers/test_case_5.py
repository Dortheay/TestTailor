import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            dict_0 = None
            int_0 = 3487
            list_0 = [dict_0, int_0, int_0]
            str_0 = None
            prepend_list_action_0 = module_0.PrependListAction(list_0, str_0, list_0, dict_0)
            tuple_0 = ()
            bool_0 = False
            prepend_list_action_1 = module_0.PrependListAction(prepend_list_action_0, prepend_list_action_0, tuple_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
