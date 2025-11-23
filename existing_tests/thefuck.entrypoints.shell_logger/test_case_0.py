import unittest
import timeout_decorator
import thefuck.entrypoints.shell_logger as module_0

class Test_Shell_logger_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = False
            var_0 = module_0.shell_logger(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
