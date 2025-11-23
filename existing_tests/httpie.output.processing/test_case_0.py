import unittest
import timeout_decorator
import httpie.output.processing as module_0

class Test_Processing_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '$)8^)FnUiI/)Xw\x0b>1'
            str_1 = '^'
            list_0 = [str_0, str_1]
            formatting_0 = module_0.Formatting(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
