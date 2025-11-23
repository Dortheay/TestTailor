import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

class Test_Option_helpers_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        argument_parser_0 = module_1.ArgumentParser()
        var_0 = module_0.add_vault_options(argument_parser_0)
        var_1 = argument_parser_0._actions
        var_2 = argument_parser_0._actions
        var_3 = argument_parser_0._actions
        var_4 = argument_parser_0._actions
        str_0 = '--ask-vault-password'
        str_1 = "'--ask-vault-password' flag names are missing"
        var_5 = argument_parser_0._actions
        var_6 = argument_parser_0._actions
        str_2 = '--vault-password-file'
        dict_0 = {str_2: str_0, str_1: var_3}
        var_7 = module_0.maybe_unfrack_path(dict_0)

if __name__ == "__main__":
    unittest.main()
