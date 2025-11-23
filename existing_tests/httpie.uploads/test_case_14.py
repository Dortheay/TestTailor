import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.uploads as module_1
import requests_toolbelt.multipart.encoder as module_2
import typing as module_3
import requests.models as module_4

class Test_Uploads_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'JV'
        dict_0 = {str_0: str_0}
        callable_0 = None
        int_0 = 1558
        var_0 = module_1.prepare_request_body(str_0, callable_0, int_0)
        tuple_0 = ()
        multipart_encoder_0 = module_2.MultipartEncoder(dict_0, tuple_0)
        var_1 = module_1.prepare_request_body(multipart_encoder_0, callable_0, int_0, int_0)
        chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        int_1 = 374
        var_2 = module_1.prepare_request_body(multipart_encoder_0, callable_0, int_1, tuple_0)
        prepared_request_0 = module_4.PreparedRequest()
        list_0 = []
        dict_1 = {}
        multipart_request_data_dict_0 = module_0.MultipartRequestDataDict(*list_0, **dict_1)
        tuple_1 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0)

if __name__ == "__main__":
    unittest.main()
