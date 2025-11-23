import unittest
import timeout_decorator
import pathlib as module_0
import httpie.sessions as module_1
import httpie.cli.dicts as module_2

class Test_Sessions_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        path_0 = module_0.Path()
        session_0 = module_1.Session(path_0)

if __name__ == "__main__":
    unittest.main()
