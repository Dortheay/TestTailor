import unittest
import timeout_decorator
import pathlib as module_0
import httpie.sessions as module_1
import httpie.cli.dicts as module_2

class Test_Sessions_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        request_headers_dict_0 = module_2.RequestHeadersDict()
        dict_0 = {}
        path_0 = module_0.Path(**dict_0)
        str_0 = '#NFv6,w\rzoN~/]!6(0Wf'
        str_1 = ''
        session_0 = module_1.get_httpie_session(path_0, str_0, str_0, str_1)
        var_0 = session_0.update_headers(request_headers_dict_0)

if __name__ == "__main__":
    unittest.main()
