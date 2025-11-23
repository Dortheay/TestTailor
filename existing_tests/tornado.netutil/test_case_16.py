import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = 'f!J.L=&w\x0b\tA:<s'
            int_0 = -359
            socket_0 = module_0.bind_unix_socket(str_0, int_0, int_0)
            s_s_l_context_0 = module_2.SSLContext()
            s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0)
            str_1 = 'WSGI support for the Tornado web framework.\n\nWSGI is the Python standard for web servers, and allows for interoperability\nbetween Tornado and other Python web frameworks and servers.\n\nThis module provides WSGI support via the `WSGIContainer` class, which\nmakes it possible to run applications using other WSGI frameworks on\nthe Tornado HTTP server. The reverse is not supported; the Tornado\n`.Application` and `.RequestHandler` classes are designed for use with\nthe Tornado `.HTTPServer` and cannot be used in a generic WSGI\ncontainer.\n\n'
            bool_0 = module_0.is_valid_ip(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
