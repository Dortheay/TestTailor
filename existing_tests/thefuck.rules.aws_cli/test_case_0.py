import unittest
import timeout_decorator
import thefuck.rules.aws_cli as module_0

class Test_Aws_cli_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '*\n %%KIO'
            var_0 = module_0.get_new_command(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
