import unittest
import timeout_decorator
import thefuck.logs as module_0

class Test_Logs_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '/ |\rGdITT\tL^9BqR\r.'
        var_0 = module_0.warn(str_0)

if __name__ == "__main__":
    unittest.main()
