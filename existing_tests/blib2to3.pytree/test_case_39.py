import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        try:
            str_0 = '0Gao\rNeF,8mJ$]a7fu#/'
            wildcard_pattern_0 = module_0.WildcardPattern(str_0)
            float_0 = -2077.620341159647
            dict_0 = {}
            bool_0 = wildcard_pattern_0.match_seq(dict_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
