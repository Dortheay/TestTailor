import unittest
import timeout_decorator
import httpie.output.processing as module_0

class Test_Processing_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '"p<'
        list_0 = []
        formatting_0 = module_0.Formatting(list_0)
        str_1 = 'O2J-jAzBGFe/Q'
        str_2 = formatting_0.format_body(str_0, str_1)
        str_3 = formatting_0.format_body(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
