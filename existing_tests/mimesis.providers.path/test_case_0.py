import unittest
import timeout_decorator
import mimesis.providers.path as module_0

class Test_Path_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            path_0 = module_0.Path()
            str_0 = path_0.home()
            str_1 = path_0.root()
            str_2 = path_0.user()
            list_0 = [str_2, str_0]
            set_0 = set()
            int_0 = -1633
            dict_0 = {str_1: set_0, str_2: int_0}
            path_1 = module_0.Path(*list_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
