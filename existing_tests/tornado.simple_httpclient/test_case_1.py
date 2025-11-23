import unittest
import timeout_decorator
import tornado.simple_httpclient as module_0

class Test_Simple_httpclient_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
