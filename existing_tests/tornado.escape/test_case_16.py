import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            bool_0 = True
            list_0 = [bool_0, bool_0]
            optional_0 = module_0.to_unicode(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
