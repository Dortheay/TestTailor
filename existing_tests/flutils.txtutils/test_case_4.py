import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            complex_0 = None
            int_0 = module_0.len_without_ansi(complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
