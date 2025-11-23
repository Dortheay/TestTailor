import unittest
import timeout_decorator
import tornado.tcpclient as module_0
import _asyncio as module_1
import tornado.netutil as module_2
import socket as module_3

class Test_Tcpclient_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            optional_0 = None
            t_c_p_client_0 = module_0.TCPClient(optional_0)
            list_0 = []
            str_0 = '.value.'
            int_0 = -2245
            dict_0 = {str_0: str_0, str_0: list_0, str_0: int_0}
            future_0 = module_1.Future(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
