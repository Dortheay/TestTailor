import unittest
import timeout_decorator
import httpie.client as module_0
import argparse as module_1
import pathlib as module_2
import httpie.cli.dicts as module_3

class Test_Client_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            namespace_0 = module_1.Namespace()
            request_headers_dict_0 = module_0.make_default_headers(namespace_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
