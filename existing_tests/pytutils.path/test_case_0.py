import unittest
import timeout_decorator
import pytutils.path as module_0

class Test_Path_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '3nh.g`Y;?;DA'
        int_0 = -4074
        var_0 = module_0.join_each(str_0, int_0)

if __name__ == "__main__":
    unittest.main()
