import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'qx'
        str_1 = module_0.xhtml_unescape(str_0)

if __name__ == "__main__":
    unittest.main()
