import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

class Test_Option_helpers_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        argument_parser_0 = module_1.ArgumentParser()
        var_0 = module_0.add_connect_options(argument_parser_0)

if __name__ == "__main__":
    unittest.main()
