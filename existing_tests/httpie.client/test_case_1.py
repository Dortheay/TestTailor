import unittest
import timeout_decorator
import httpie.client as module_0
import argparse as module_1
import pathlib as module_2
import httpie.cli.dicts as module_3

class Test_Client_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = {}
            var_0 = module_0.dump_request(dict_0)
            namespace_0 = module_1.Namespace()
            dict_1 = module_0.make_request_kwargs(namespace_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
