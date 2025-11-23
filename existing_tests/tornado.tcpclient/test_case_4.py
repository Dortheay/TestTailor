import unittest
import timeout_decorator
import tornado.tcpclient as module_0
import _asyncio as module_1
import tornado.netutil as module_2
import socket as module_3

class Test_Tcpclient_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            future_0 = None
            address_family_0 = module_3.AddressFamily.AF_APPLETALK
            int_0 = 1431
            str_0 = '{'
            int_1 = 35
            resolver_0 = module_2.Resolver()
            awaitable_0 = resolver_0.resolve(str_0, int_1, address_family_0)
            str_1 = 'IPPROTO_IPV6'
            list_0 = [int_0, str_1, int_1]
            tuple_0 = (int_0, awaitable_0, list_0)
            tuple_1 = (address_family_0, tuple_0)
            list_1 = [tuple_1]
            tuple_2 = (list_1, list_1)
            t_c_p_client_0 = module_0.TCPClient()
            i_o_stream_0 = t_c_p_client_0.connect(str_1, int_0)
            tuple_3 = (future_0, tuple_2, i_o_stream_0)
            t_c_p_client_1 = module_0.TCPClient(tuple_3)
            t_c_p_client_1.close()
            bytes_0 = b"'@\x1f\x18\x0cW\xd1\x87\xddv\xbb\\\xa4\xb0\x88s\xfbU\x12\x90"
            tuple_4 = (bytes_0,)
            list_2 = [tuple_4, tuple_4, tuple_4, tuple_4]
            list_3 = []
            dict_0 = {}
            resolver_1 = module_2.Resolver(*list_3, **dict_0)
            connector_0 = module_0._Connector(list_2, resolver_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
