import unittest
import timeout_decorator
import httpie.output.processing as module_0

class Test_Processing_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        conversion_0 = module_0.Conversion()
        str_0 = '.jm:z?f/%jVl^k@e;'
        optional_0 = conversion_0.get_converter(str_0)

if __name__ == "__main__":
    unittest.main()
