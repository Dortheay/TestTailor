import unittest
import timeout_decorator
import mimesis.providers.path as module_0

class Test_Path_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'linux'
        path_0 = module_0.Path(str_0)
        str_1 = 'win32'
        path_1 = module_0.Path(str_1)
        str_2 = path_1.user()

if __name__ == "__main__":
    unittest.main()
