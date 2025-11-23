import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '%s not found in named urls'
            bool_0 = True
            str_1 = 'm'
            list_0 = [str_0, str_0, str_1]
            any_0 = module_0.recursive_unicode(str_1)
            str_2 = module_0.linkify(str_0, str_0, bool_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
