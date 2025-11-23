import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

class Test_Option_helpers_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        argument_parser_0 = module_1.ArgumentParser()
        var_0 = module_0.add_inventory_options(argument_parser_0)
        str_0 = '--inventory'
        str_1 = 'hosts'
        str_2 = [str_0, str_1]
        var_1 = argument_parser_0.parse_args(str_2)
        str_3 = '--list-hosts'
        str_4 = [str_3]
        var_2 = argument_parser_0.parse_args(str_4)
        str_5 = '--limit'
        str_6 = 'subset_pattern'
        str_7 = [str_5, str_6]
        var_3 = argument_parser_0.parse_args(str_7)

if __name__ == "__main__":
    unittest.main()
