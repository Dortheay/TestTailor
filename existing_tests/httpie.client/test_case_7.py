import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.client as module_1
import argparse as module_2

class Test_Client_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        request_headers_dict_0 = module_0.RequestHeadersDict()
        request_headers_dict_1 = module_1.finalize_headers(request_headers_dict_0)

if __name__ == "__main__":
    unittest.main()
