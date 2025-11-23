import unittest
import timeout_decorator
import flutils.codecs.raw_utf8_escape as module_0

class Test_Raw_utf8_escape_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'q('
        tuple_0 = module_0.encode(str_0)

if __name__ == "__main__":
    unittest.main()
