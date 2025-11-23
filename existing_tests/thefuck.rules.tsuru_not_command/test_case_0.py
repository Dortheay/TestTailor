import unittest
import timeout_decorator
import thefuck.rules.tsuru_not_command as module_0

class Test_Tsuru_not_command_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '^8Ye&sb5&~kuQp5|@A/$'
            var_0 = module_0.match(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
