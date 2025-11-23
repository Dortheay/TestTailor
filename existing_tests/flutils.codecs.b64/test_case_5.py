import unittest
import timeout_decorator
import flutils.codecs.b64 as module_0
import collections as module_1
import codecs as module_2

class Test_B64_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            module_0.register()
            module_0.register()
            str_0 = None
            int_0 = 12
            tuple_0 = (str_0, int_0)
            tuple_1 = module_0.decode(tuple_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
