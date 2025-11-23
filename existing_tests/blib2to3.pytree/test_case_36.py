import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_37(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        try:
            str_0 = '<^TvP$'
            wildcard_pattern_0 = module_0.WildcardPattern(str_0)
            int_0 = 59
            wildcard_pattern_1 = module_0.WildcardPattern(str_0, int_0, int_0)
            str_1 = '\t\\'
            set_0 = {str_1, wildcard_pattern_1}
            bool_0 = wildcard_pattern_1.match_seq(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
