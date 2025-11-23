import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

class Test_Option_helpers_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        var_0 = module_0.version()
        bytes_0 = b'\x02:\xb9\xeeW^\xe1\xf6\x06\x07\xf0'
        tuple_0 = ()
        str_0 = '9lo"/[,6kw)YqP'
        str_1 = 'gEm%YAM=4'
        list_0 = [str_0, str_1, tuple_0]
        set_0 = None
        prepend_list_action_0 = module_0.PrependListAction(tuple_0, set_0, bytes_0)
        prepend_list_action_1 = module_0.PrependListAction(bytes_0, prepend_list_action_0)
        float_0 = 772.03342
        var_1 = module_0.create_base_parser(float_0, set_0, float_0)
        int_0 = 999
        sorting_help_formatter_0 = None
        float_1 = -66.98441938319507
        list_1 = [prepend_list_action_1, var_1]
        namespace_0 = module_1.Namespace()
        prepend_list_action_2 = module_0.PrependListAction(list_1, float_1, namespace_0, sorting_help_formatter_0, tuple_0)
        unrecognized_argument_0 = module_0.UnrecognizedArgument(list_0, namespace_0, int_0)
        str_2 = 'q&:);AzYm'
        var_2 = module_0.ensure_value(unrecognized_argument_0, str_2, bytes_0)

if __name__ == "__main__":
    unittest.main()
