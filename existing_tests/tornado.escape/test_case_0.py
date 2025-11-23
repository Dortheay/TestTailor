import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'verbose'
            optional_0 = module_0.utf8(str_0)
            str_1 = module_0.xhtml_escape(str_0)
            str_2 = module_0.json_encode(optional_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
