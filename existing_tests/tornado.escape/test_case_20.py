import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '|3^Nifo:9B#\t,|&{^u'
        var_0 = module_0.url_unescape(str_0)

if __name__ == "__main__":
    unittest.main()
