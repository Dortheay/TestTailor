import unittest
import timeout_decorator
import mimesis.providers.path as module_0

class Test_Path_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        path_0 = module_0.Path()
        str_0 = path_0.project_dir()

if __name__ == "__main__":
    unittest.main()
