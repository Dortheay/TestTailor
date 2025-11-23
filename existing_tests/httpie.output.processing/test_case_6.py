import unittest
import timeout_decorator
import httpie.output.processing as module_0

class Test_Processing_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = None
        conversion_0 = module_0.Conversion()
        optional_0 = conversion_0.get_converter(str_0)
        conversion_1 = module_0.Conversion()

if __name__ == "__main__":
    unittest.main()
