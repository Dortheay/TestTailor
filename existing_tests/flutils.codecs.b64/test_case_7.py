import unittest
import timeout_decorator
import flutils.codecs.b64 as module_0
import collections as module_1
import codecs as module_2

class Test_B64_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            module_0.register()
            byte_string_0 = None
            tuple_0 = module_0.decode(byte_string_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
