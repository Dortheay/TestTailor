import unittest
import timeout_decorator
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests.models as module_2
import typing as module_3
import requests_toolbelt.multipart.encoder as module_4

class Test_Uploads_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = ' R'
            dict_0 = {str_0: str_0}
            dict_1 = {str_0: str_0}
            chunked_upload_stream_0 = module_0.ChunkedUploadStream(dict_1, str_0)
            tuple_0 = ()
            multipart_encoder_0 = module_4.MultipartEncoder(dict_0, tuple_0)
            chunked_multipart_upload_stream_0 = module_0.ChunkedMultipartUploadStream(multipart_encoder_0)
            prepared_request_0 = module_2.PreparedRequest()
            var_0 = module_0.prepare_request_body(multipart_encoder_0, prepared_request_0)
            prepared_request_1 = module_2.PreparedRequest()
            bool_0 = True
            var_1 = module_0.compress_request(prepared_request_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
