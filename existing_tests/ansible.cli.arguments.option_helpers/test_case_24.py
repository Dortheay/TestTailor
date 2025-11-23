import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

class Test_Option_helpers_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        tuple_0 = None
        float_0 = -3169.04
        str_0 = '1acyAap'
        unrecognized_argument_0 = module_0.UnrecognizedArgument(tuple_0, float_0, str_0, tuple_0)
        int_0 = 511
        ansible_version_0 = None
        var_0 = module_0.create_base_parser(int_0, ansible_version_0)

if __name__ == "__main__":
    unittest.main()
