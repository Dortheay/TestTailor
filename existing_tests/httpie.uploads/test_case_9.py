import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.uploads as module_1
import requests_toolbelt.multipart.encoder as module_2
import typing as module_3
import requests.models as module_4

class Test_Uploads_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        multipart_request_data_dict_0 = module_0.MultipartRequestDataDict()
        tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0)

if __name__ == "__main__":
    unittest.main()
