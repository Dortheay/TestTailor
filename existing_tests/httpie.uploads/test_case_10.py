import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.uploads as module_1
import requests_toolbelt.multipart.encoder as module_2
import typing as module_3
import requests.models as module_4

class Test_Uploads_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'Range'
        dict_0 = {str_0: str_0}
        float_0 = -1396.516328
        chunked_upload_stream_0 = module_1.ChunkedUploadStream(dict_0, float_0)
        iterable_0 = chunked_upload_stream_0.__iter__()

if __name__ == "__main__":
    unittest.main()
