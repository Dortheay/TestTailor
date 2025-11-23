import unittest
import timeout_decorator
import httpie.output.processing as module_0

class Test_Processing_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        conversion_0 = module_0.Conversion()

if __name__ == "__main__":
    unittest.main()
