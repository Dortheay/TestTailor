import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

class Test_Option_helpers_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        var_0 = module_0.unfrack_path()
        var_1 = module_0.version()

if __name__ == "__main__":
    unittest.main()
