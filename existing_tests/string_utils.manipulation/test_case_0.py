import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        string_compressor_0 = module_0.__StringCompressor()

if __name__ == "__main__":
    unittest.main()
