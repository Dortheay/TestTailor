import unittest
import timeout_decorator
import thefuck.logs as module_0

class Test_Logs_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'Test debug message'
        var_0 = module_0.debug(str_0)

if __name__ == "__main__":
    unittest.main()
