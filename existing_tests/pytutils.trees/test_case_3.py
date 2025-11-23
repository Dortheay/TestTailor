import unittest
import timeout_decorator
import pytutils.trees as module_0

class Test_Trees_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = None
            tree_0 = module_0.Tree()
            var_0 = tree_0.__getitem__(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
