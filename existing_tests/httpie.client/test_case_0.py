import unittest
import timeout_decorator
import httpie.client as module_0
import argparse as module_1
import pathlib as module_2
import httpie.cli.dicts as module_3

class Test_Client_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = False
            session_0 = module_0.build_requests_session(bool_0)
            namespace_0 = module_1.Namespace()
            dict_0 = module_0.make_send_kwargs_mergeable_from_env(namespace_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
