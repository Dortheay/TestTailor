import unittest
import timeout_decorator
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests.models as module_2
import typing as module_3
import requests_toolbelt.multipart.encoder as module_4

class Test_Uploads_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            chunked_upload_stream_0 = None
            dict_0 = {chunked_upload_stream_0: chunked_upload_stream_0}
            request_data_dict_0 = module_1.RequestDataDict()
            callable_0 = None
            list_0 = [request_data_dict_0]
            int_0 = None
            var_0 = module_0.prepare_request_body(request_data_dict_0, callable_0, list_0, int_0)
            callable_1 = None
            chunked_upload_stream_1 = module_0.ChunkedUploadStream(dict_0, callable_1)
            prepared_request_0 = module_2.PreparedRequest()
            i_o_0 = module_3.IO()
            dict_1 = {}
            multipart_request_data_dict_0 = module_1.MultipartRequestDataDict(**dict_1)
            prepared_request_1 = module_2.PreparedRequest()
            bool_0 = True
            var_1 = module_0.compress_request(prepared_request_1, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
