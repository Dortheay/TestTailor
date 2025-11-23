import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = -2623
            var_0 = module_0.add_module_options(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
