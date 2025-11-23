import unittest
import timeout_decorator
import mimesis.providers.path as module_0

class Test_Path_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        path_0 = module_0.Path()
        str_0 = path_0.home()

if __name__ == "__main__":
    unittest.main()
