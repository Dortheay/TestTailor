import unittest
import timeout_decorator
import flutils.codecs.raw_utf8_escape as module_0

class Test_Raw_utf8_escape_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'QVh7N/>\x0bc\x0cuxIEkwu8'
        tuple_0 = module_0.encode(str_0)

if __name__ == "__main__":
    unittest.main()
