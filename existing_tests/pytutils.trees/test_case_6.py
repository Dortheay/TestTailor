import unittest
import timeout_decorator
import pytutils.trees as module_0

class Test_Trees_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            var_0 = module_0.tree()
            tree_0 = module_0.Tree()
            str_0 = '\rk\nl}S;'
            bool_0 = True
            var_1 = tree_0.__getitem__(str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
