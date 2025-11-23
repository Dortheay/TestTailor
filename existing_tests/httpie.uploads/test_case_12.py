import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.uploads as module_1
import requests_toolbelt.multipart.encoder as module_2
import typing as module_3
import requests.models as module_4

class Test_Uploads_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bytes_0 = b'\xf8.\xb3Y\xcd?\x94?\xb2C\x02l'
        callable_0 = None
        var_0 = module_1.prepare_request_body(bytes_0, callable_0)

if __name__ == "__main__":
    unittest.main()
