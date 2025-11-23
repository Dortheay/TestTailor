import unittest
import timeout_decorator
import thefuck.entrypoints.fix_command as module_0

class Test_Fix_command_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = ''
            var_0 = module_0.fix_command(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
