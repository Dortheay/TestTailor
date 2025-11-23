import unittest
import timeout_decorator
import httpie.client as module_0
import argparse as module_1
import pathlib as module_2
import httpie.cli.dicts as module_3

class Test_Client_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            namespace_0 = module_1.Namespace()
            bool_0 = False
            str_0 = '{0}:{1:0>2}:{2:0>2}'
            session_0 = module_0.build_requests_session(bool_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
