import unittest
import timeout_decorator
import tornado.netutil as module_0
import tornado.tcpclient as module_1

class Test_Tcpclient_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        resolver_0 = module_0.Resolver()
        t_c_p_client_0 = module_1.TCPClient(resolver_0)

if __name__ == "__main__":
    unittest.main()
