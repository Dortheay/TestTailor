import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            int_0 = 805
            str_0 = 'XqEUB"o{3?Q]5Ls,;'
            list_0 = [str_0, str_0, str_0]
            leaf_0 = module_0.Leaf(int_0, str_0, str_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
