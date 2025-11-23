import unittest
import timeout_decorator
import httpie.uploads as module_0
import httpie.cli.dicts as module_1
import requests.models as module_2
import typing as module_3
import requests_toolbelt.multipart.encoder as module_4

class Test_Uploads_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = ']!JI7f'
            dict_0 = {}
            var_0 = module_0.prepare_request_body(str_0, dict_0)
            prepared_request_0 = module_2.PreparedRequest()
            multipart_request_data_dict_0 = module_1.MultipartRequestDataDict()
            i_o_0 = module_3.IO()
            callable_0 = None
            var_1 = module_0.prepare_request_body(i_o_0, callable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
