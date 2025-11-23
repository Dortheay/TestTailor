import unittest
import timeout_decorator
import pathlib as module_0
import httpie.sessions as module_1
import httpie.cli.dicts as module_2

class Test_Sessions_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        path_0 = module_0.Path()
        str_0 = 'kPFdWS4rd<3'
        session_0 = module_1.get_httpie_session(path_0, str_0, str_0, str_0)
        str_1 = 'A'
        session_1 = module_1.Session(str_1)

if __name__ == "__main__":
    unittest.main()
