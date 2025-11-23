import unittest
import timeout_decorator
import tornado.tcpclient as module_0
import _asyncio as module_1
import tornado.netutil as module_2
import socket as module_3

class Test_Tcpclient_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            optional_0 = None
            t_c_p_client_0 = module_0.TCPClient(optional_0)
            t_c_p_client_0.close()
            bool_0 = True
            str_0 = '43M,l_w^\r3p('
            int_0 = 416
            resolver_0 = module_2.Resolver()
            awaitable_0 = resolver_0.resolve(str_0, int_0)
            tuple_0 = (bool_0, awaitable_0)
            list_0 = [tuple_0, tuple_0]
            str_1 = '^"uPN6SkG3'
            int_1 = 1785
            address_family_0 = module_3.AddressFamily.AF_APPLETALK
            i_o_stream_0 = t_c_p_client_0.connect(str_1, int_1, address_family_0)
            connector_0 = module_0._Connector(list_0, i_o_stream_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
