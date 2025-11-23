import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

class Test_Option_helpers_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        argument_parser_0 = module_1.ArgumentParser()
        var_0 = module_0.add_subset_options(argument_parser_0)
        str_0 = '-t'
        var_1 = argument_parser_0.parse_args(str_0)

if __name__ == "__main__":
    unittest.main()
