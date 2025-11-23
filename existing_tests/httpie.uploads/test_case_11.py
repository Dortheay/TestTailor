import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.uploads as module_1
import requests_toolbelt.multipart.encoder as module_2
import typing as module_3
import requests.models as module_4

class Test_Uploads_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'field2'
        str_1 = 'value2'
        str_2 = {str_0: str_1}
        multipart_encoder_0 = module_2.MultipartEncoder(str_2)
        chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        iterable_0 = chunked_multipart_upload_stream_0.__iter__()
        var_0 = list(iterable_0)
        var_1 = len(var_0)

if __name__ == "__main__":
    unittest.main()
