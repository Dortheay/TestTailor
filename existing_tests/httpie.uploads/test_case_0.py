import unittest
import timeout_decorator
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests.models as module_2
import typing as module_3
import requests_toolbelt.multipart.encoder as module_4

class Test_Uploads_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            var_0 = lambda chunk: tracked_chunks.append(chunk)
            bytes_0 = b'chunk1'
            bytes_1 = b'chunk2'
            bytes_2 = b'chunk3'
            bytes_3 = [bytes_0, bytes_1, bytes_2]
            chunked_upload_stream_0 = module_0.ChunkedUploadStream(bytes_3, var_0)
            var_1 = list(chunked_upload_stream_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
