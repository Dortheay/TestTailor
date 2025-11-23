import unittest
import timeout_decorator
import thefuck.logs as module_0

class Test_Logs_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = "cp: cannot create regular file '([^']*)': No such file or directory"
        var_0 = module_0.failed(str_0)

if __name__ == "__main__":
    unittest.main()
