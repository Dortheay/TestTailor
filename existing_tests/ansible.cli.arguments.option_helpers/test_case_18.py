import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            var_0 = module_0.unfrack_path()
            bool_0 = False
            var_1 = module_0.add_tasknoplay_options(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
