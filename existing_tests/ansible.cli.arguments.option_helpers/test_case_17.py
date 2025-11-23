import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            var_0 = module_0.unfrack_path()
            str_0 = '9luXV@:c%-!qS%=+'
            var_1 = module_0.add_check_options(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
