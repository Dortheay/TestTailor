import unittest
import timeout_decorator
import httpie.client as module_0
import argparse as module_1
import pathlib as module_2
import httpie.cli.dicts as module_3

class Test_Client_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'x\n?DZKg8?5I6\x0b`1'
            bool_0 = True
            session_0 = module_0.build_requests_session(bool_0)
            dict_0 = {str_0: str_0, str_0: session_0}
            session_1 = module_0.build_requests_session(bool_0)
            str_1 = 'WzVty\tXy\rd'
            str_2 = 'Content-Disposition'
            str_3 = module_0.ensure_path_as_is(str_1, str_2)
            namespace_0 = module_1.Namespace(**dict_0)
            path_0 = module_2.Path(**dict_0)
            namespace_1 = module_1.Namespace()
            bool_1 = True
            session_2 = module_0.build_requests_session(bool_1)
            iterable_0 = module_0.collect_messages(namespace_1, path_0)
            request_headers_dict_0 = module_3.RequestHeadersDict(iterable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
