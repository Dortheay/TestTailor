import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = 908
            int_1 = -1642
            var_0 = module_0.version(int_1)
            var_1 = module_0.add_runtask_options(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
