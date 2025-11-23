import unittest
import timeout_decorator
import flutils.codecs.b64 as module_0
import collections as module_1
import codecs as module_2

class Test_B64_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '\x0c_t~sHNz5)4gvhyAA!'
            list_0 = [str_0, str_0, str_0]
            tuple_0 = module_0.decode(list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
