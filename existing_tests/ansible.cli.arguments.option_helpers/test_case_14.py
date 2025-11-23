import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            var_0 = module_0.unfrack_path()
            var_1 = module_0.version()
            bool_0 = False
            var_2 = module_0.add_output_options(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
