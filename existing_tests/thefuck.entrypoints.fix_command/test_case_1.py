import unittest
import timeout_decorator
import thefuck.entrypoints.fix_command as module_0

class Test_Fix_command_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 2499
            var_0 = module_0.fix_command(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
