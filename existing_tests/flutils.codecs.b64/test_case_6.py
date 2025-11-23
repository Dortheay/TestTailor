import unittest
import timeout_decorator
import flutils.codecs.b64 as module_0
import collections as module_1
import codecs as module_2

class Test_B64_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'b64>q'
            var_0 = module_2.getdecoder(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
