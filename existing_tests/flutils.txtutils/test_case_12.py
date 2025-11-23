import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bool_0 = False
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_0, bool_0)

if __name__ == "__main__":
    unittest.main()
