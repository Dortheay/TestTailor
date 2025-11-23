import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = None
            str_0 = 'D*}HXm;h}EzG/'
            dict_0 = {str_0: int_0}
            int_1 = -2143
            str_1 = 'm(Q6B'
            list_0 = [dict_0, dict_0]
            leaf_0 = module_0.Leaf(int_1, str_1, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
