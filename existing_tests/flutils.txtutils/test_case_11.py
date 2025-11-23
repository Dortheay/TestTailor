import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '3F'
        int_0 = module_0.len_without_ansi(str_0)

if __name__ == "__main__":
    unittest.main()
