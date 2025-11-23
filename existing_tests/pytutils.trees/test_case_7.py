import unittest
import timeout_decorator
import pytutils.trees as module_0

class Test_Trees_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            tree_0 = module_0.Tree()
            str_0 = '\x0c02w'
            int_0 = 600
            var_0 = tree_0.__setitem__(str_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
