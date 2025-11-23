import unittest
import timeout_decorator
import httpie.output.processing as module_0

class Test_Processing_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '"p<'
        list_0 = []
        formatting_0 = module_0.Formatting(list_0)
        str_1 = formatting_0.format_body(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
