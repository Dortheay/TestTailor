import unittest
import timeout_decorator
import flutils.codecs.raw_utf8_escape as module_0

class Test_Raw_utf8_escape_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        module_0.register()

if __name__ == "__main__":
    unittest.main()
