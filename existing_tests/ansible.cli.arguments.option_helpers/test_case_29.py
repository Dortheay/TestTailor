import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

class Test_Option_helpers_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        argument_parser_0 = module_1.ArgumentParser()
        var_0 = module_0.add_vault_options(argument_parser_0)
        var_1 = argument_parser_0._actions
        var_2 = argument_parser_0._actions
        var_3 = argument_parser_0._actions
        var_4 = argument_parser_0._actions
        var_5 = argument_parser_0._actions
        var_6 = argument_parser_0._actions

if __name__ == "__main__":
    unittest.main()
