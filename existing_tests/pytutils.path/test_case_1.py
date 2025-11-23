import unittest
import timeout_decorator
import pytutils.path as module_0

class Test_Path_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '/home/user'
        str_1 = 'docs'
        str_2 = 'photos'
        str_3 = 'music'
        str_4 = [str_1, str_2, str_3]
        var_0 = module_0.join_each(str_0, str_4)
        var_1 = list(var_0)

if __name__ == "__main__":
    unittest.main()
