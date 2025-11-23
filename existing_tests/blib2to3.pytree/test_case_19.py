import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'PatternGrammar.txt'
            wildcard_pattern_0 = module_0.WildcardPattern(str_0)
            bool_0 = wildcard_pattern_0.match_seq(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
