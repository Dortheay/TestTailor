import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'suz]sGos%}gyv9f2G'
            int_0 = 211
            str_1 = ')Z'
            set_0 = set()
            str_2 = "Reboot command failed. Error was: '{stdout}, {stderr}'"
            int_1 = 79
            set_1 = {int_0, str_0}
            unrecognized_argument_0 = module_0.UnrecognizedArgument(int_1, set_1)
            var_0 = unrecognized_argument_0.__call__(set_0, str_1, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
