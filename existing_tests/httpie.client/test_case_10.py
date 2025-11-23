import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.client as module_1
import argparse as module_2

class Test_Client_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        namespace_0 = module_2.Namespace()
        str_0 = '+3R :y"g'
        dict_0 = {str_0: str_0}
        bool_0 = True
        session_0 = module_1.build_requests_session(bool_0)
        request_headers_dict_0 = module_0.RequestHeadersDict(**dict_0)
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)
        request_headers_dict_2 = module_1.finalize_headers(request_headers_dict_1)

if __name__ == "__main__":
    unittest.main()
