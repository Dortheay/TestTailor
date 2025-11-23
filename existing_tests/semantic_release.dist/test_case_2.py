import unittest
import timeout_decorator
import semantic_release.dist as module_0

class Test_Dist_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            var_0 = module_0.should_remove_dist()
            var_1 = module_0.build_dists()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
