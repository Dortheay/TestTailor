import unittest
import timeout_decorator
import thefuck.rules.sudo_command_from_user_path as module_0

class Test_Sudo_command_from_user_path_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 1599.9095
            var_0 = module_0.get_new_command(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
