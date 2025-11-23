import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.sessions as module_1
import pathlib as module_2

class Test_Sessions_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = ')P~_\rZ<]'
            str_1 = 'DownloadRfde implement^tion.\n\n'
            list_0 = [str_0, str_0, str_0, str_1]
            str_2 = 'cookie'
            dict_0 = {str_2: str_2, str_1: str_1, str_0: str_0, str_0: str_0, str_1: list_0, str_2: str_2}
            request_headers_dict_0 = module_0.RequestHeadersDict(dict_0, **dict_0)
            session_0 = module_1.Session(str_1)
            var_0 = session_0.update_headers(request_headers_dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
