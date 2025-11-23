import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'gatternGramm|r.txt'
            wildcard_pattern_0 = module_0.WildcardPattern(str_0)
            int_0 = 3992
            str_1 = ''
            node_pattern_0 = module_0.NodePattern(int_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
