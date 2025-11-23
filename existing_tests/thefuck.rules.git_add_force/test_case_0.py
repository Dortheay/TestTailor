import unittest
import timeout_decorator
import thefuck.rules.git_add_force as module_0

class Test_Git_add_force_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'gHa}^OKs%\\(@7]]'
            var_0 = module_0.get_new_command(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
