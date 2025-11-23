import unittest
import timeout_decorator
import collections as module_0
import flutils.codecs.raw_utf8_escape as module_1
import codecs as module_2

class Test_Raw_utf8_escape_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            module_1.register()
            str_0 = None
            tuple_0 = module_1.decode(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
