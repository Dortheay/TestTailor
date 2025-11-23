import unittest
import timeout_decorator
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests.models as module_2
import typing as module_3
import requests_toolbelt.multipart.encoder as module_4

class Test_Uploads_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = ']!JI7f'
            multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
            tuple_0 = module_0.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0, str_0)
            dict_0 = {}
            var_0 = module_0.prepare_request_body(str_0, dict_0)
            iterable_0 = None
            prepared_request_0 = module_2.PreparedRequest()
            multipart_request_data_dict_1 = module_1.MultipartRequestDataDict()
            int_0 = 4248
            str_1 = 'value'
            var_1 = module_0.prepare_request_body(str_0, multipart_request_data_dict_1, int_0, str_1)
            chunked_upload_stream_0 = module_0.ChunkedUploadStream(iterable_0, multipart_request_data_dict_0)
            bool_0 = False
            var_2 = module_0.compress_request(prepared_request_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
