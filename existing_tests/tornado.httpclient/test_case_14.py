import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            module_0.main()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
