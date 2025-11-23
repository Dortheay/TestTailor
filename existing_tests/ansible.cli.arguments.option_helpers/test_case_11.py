import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = 'M5_QtekA&988[Oc$/++'
            var_0 = module_0.add_fork_options(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
