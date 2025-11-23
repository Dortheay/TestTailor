import unittest
import timeout_decorator
import semantic_release.dist as module_0

class Test_Dist_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        var_0 = module_0.should_remove_dist()

if __name__ == "__main__":
    unittest.main()
