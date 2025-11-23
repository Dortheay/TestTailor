import unittest
import timeout_decorator
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests.models as module_2
import typing as module_3
import requests_toolbelt.multipart.encoder as module_4

class Test_Uploads_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            prepared_request_0 = module_2.PreparedRequest()
            bool_0 = False
            var_0 = module_0.compress_request(prepared_request_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
