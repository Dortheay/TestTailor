import unittest
import timeout_decorator
import pathlib as module_0
import httpie.sessions as module_1
import httpie.cli.dicts as module_2

class Test_Sessions_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'test_session.json'
        session_0 = module_1.Session(str_0)
        str_1 = 'User-Agent'
        str_2 = 'Content-Type'
        str_3 = 'Authorization'
        str_4 = 'Cookie'
        str_5 = 'HTTPie/2.4.0'
        str_6 = 'application/json'
        str_7 = 'Bearer token123'
        str_8 = 'sessionid=abc123; csrftoken=def456'
        str_9 = {str_1: str_5, str_2: str_6, str_3: str_7, str_4: str_8}
        request_headers_dict_0 = module_2.RequestHeadersDict(str_9)
        var_0 = session_0.update_headers(request_headers_dict_0)

if __name__ == "__main__":
    unittest.main()
