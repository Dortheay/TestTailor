import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'Check out http://example.com for more info.'
        str_1 = module_0.linkify(str_0)
        str_2 = 'Visit http://example.com/some/very/long/url/that/needs/to/be/shortened'
        bool_0 = True
        str_3 = module_0.linkify(str_2, bool_0)
        str_4 = 'Go to www.example.com for details.'
        str_5 = module_0.linkify(str_4, bool_0)
        str_6 = 'Access ftp://files.example.com here.'
        str_7 = 'ftp'
        str_8 = [str_7]
        str_9 = module_0.linkify(str_6, str_8)
        str_10 = 'Check this out: http://example.com'
        str_11 = 'rel="nofollow"'
        str_12 = module_0.linkify(str_10, str_11)

if __name__ == "__main__":
    unittest.main()
