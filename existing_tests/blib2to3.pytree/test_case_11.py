import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 256
            var_0 = module_0.type_repr(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
