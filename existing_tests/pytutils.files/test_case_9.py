import unittest
import timeout_decorator
import pytutils.files as module_0

class Test_Files_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = 548
        var_0 = module_0.islurp(int_0)

if __name__ == "__main__":
    unittest.main()
