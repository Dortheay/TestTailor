import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = '0Gao\rNeF,8mJ$]a7fu#/'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        tuple_0 = ()
        bool_0 = wildcard_pattern_0.match_seq(tuple_0)

if __name__ == "__main__":
    unittest.main()
