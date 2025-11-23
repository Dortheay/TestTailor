import unittest
import timeout_decorator
import tornado.tcpclient as module_0
import _asyncio as module_1
import tornado.netutil as module_2
import socket as module_3

class Test_Tcpclient_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            tuple_0 = ()
            list_0 = [tuple_0, tuple_0, tuple_0]
            float_0 = 1.0
            connector_0 = module_0._Connector(list_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
