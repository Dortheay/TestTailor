import unittest
import timeout_decorator
import thefuck.rules.no_such_file as module_0

class Test_No_such_file_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = ' 2 '
            var_0 = module_0.get_new_command(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
