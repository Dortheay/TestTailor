import unittest
import timeout_decorator
import tornado.netutil as module_0
import ssl as module_1

class Test_Netutil_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '/<j'
        bool_0 = module_0.is_valid_ip(str_0)

if __name__ == "__main__":
    unittest.main()
