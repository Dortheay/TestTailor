import unittest
import timeout_decorator
import httpie.cli.dicts as module_0
import httpie.sessions as module_1
import pathlib as module_2

class Test_Sessions_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            path_0 = module_2.Path()
            session_0 = module_1.Session(path_0)
            var_0 = session_0.remove_cookies(path_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
