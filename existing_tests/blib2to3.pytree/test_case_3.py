import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '(?:[uUrRbBfF]|[rR][fFbB]|[fFbBuU][rR])?'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)

if __name__ == "__main__":
    unittest.main()
