import unittest
import timeout_decorator
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests.models as module_2
import typing as module_3
import requests_toolbelt.multipart.encoder as module_4

class Test_Uploads_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = ']!JI7f'
            dict_0 = {}
            var_0 = module_0.prepare_request_body(str_0, dict_0)
            prepared_request_0 = module_2.PreparedRequest()
            multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
            int_0 = 4248
            str_1 = 'K"Q\\}zZDE}<uT'
            var_1 = module_0.prepare_request_body(str_0, multipart_request_data_dict_0, int_0, str_1)
            bool_0 = False
            var_2 = module_0.compress_request(prepared_request_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
