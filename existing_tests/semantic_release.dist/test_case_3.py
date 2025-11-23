import unittest
import timeout_decorator
import semantic_release.dist as module_0

class Test_Dist_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'retry'
            var_0 = module_0.remove_dists(str_0)
            var_1 = module_0.build_dists()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
