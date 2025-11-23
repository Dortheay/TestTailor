import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = 'gatternGramm|r.txt'
            wildcard_pattern_0 = module_0.WildcardPattern(str_0)
            int_0 = 3319
            list_0 = []
            node_0 = module_0.Node(int_0, list_0, str_0)
            bool_0 = wildcard_pattern_0.match_seq(node_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
