import unittest
import timeout_decorator
import httpie.output.processing as module_0

class Test_Processing_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'qY!YJq\\|s\x0b_Q\r0A^45'
        conversion_0 = module_0.Conversion()
        optional_0 = conversion_0.get_converter(str_0)

if __name__ == "__main__":
    unittest.main()
