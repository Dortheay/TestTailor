import unittest
import timeout_decorator
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests.models as module_2
import typing as module_3
import requests_toolbelt.multipart.encoder as module_4

class Test_Uploads_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = ' R'
            dict_0 = {str_0: str_0}
            dict_1 = {str_0: str_0}
            chunked_upload_stream_0 = module_0.ChunkedUploadStream(dict_1, str_0)
            iterable_0 = chunked_upload_stream_0.__iter__()
            prepared_request_0 = module_2.PreparedRequest()
            prepared_request_1 = module_2.PreparedRequest()
            bool_0 = True
            int_0 = -840
            str_1 = '--cert'
            bytes_0 = b'i ?\xf1eL\xc6yu={\xea\xff\x14c|'
            var_0 = module_0.prepare_request_body(str_0, int_0, int_0, str_1, bytes_0)
            multipart_request_data_dict_0 = module_1.MultipartRequestDataDict(**dict_0)
            var_1 = module_0.compress_request(prepared_request_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
