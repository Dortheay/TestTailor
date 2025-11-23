import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.uploads as module_1
import requests_toolbelt.multipart.encoder as module_2
import typing as module_3
import requests.models as module_4

class Test_Uploads_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        i_o_0 = module_3.IO()
        var_0 = i_o_0.__enter__()
        prepared_request_0 = module_4.PreparedRequest()
        int_0 = -4653
        var_1 = i_o_0.readline(int_0)
        int_1 = i_o_0.write(var_1)
        set_0 = {prepared_request_0, i_o_0, i_o_0, int_0}
        int_2 = 1644
        str_0 = 'Unknown output options: {0}={1}'
        multipart_encoder_0 = None
        str_1 = None
        tuple_0 = (multipart_encoder_0, str_1)
        chunked_upload_stream_0 = module_1.ChunkedUploadStream(str_0, tuple_0)
        iterable_0 = chunked_upload_stream_0.__iter__()
        float_0 = 0.1
        chunked_upload_stream_1 = module_1.ChunkedUploadStream(iterable_0, float_0)
        var_2 = module_1.prepare_request_body(i_o_0, set_0, int_1, prepared_request_0, int_2)
        chunked_upload_stream_2 = module_1.ChunkedUploadStream(var_0, prepared_request_0)
        chunked_upload_stream_3 = module_1.ChunkedUploadStream(chunked_upload_stream_2, chunked_upload_stream_2)

if __name__ == "__main__":
    unittest.main()
