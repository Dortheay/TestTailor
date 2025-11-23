import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

class Test_Option_helpers_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        argument_parser_0 = module_1.ArgumentParser()
        var_0 = module_0.add_runas_options(argument_parser_0)
        str_0 = '-b'
        str_1 = '--become-method'
        str_2 = 'sudo'
        str_3 = '--become-user'
        str_4 = 'admin'
        str_5 = [str_0, str_1, str_2, str_3, str_4]
        var_1 = argument_parser_0.parse_args(str_5)
        var_2 = []
        var_3 = argument_parser_0.parse_args(var_2)

if __name__ == "__main__":
    unittest.main()
