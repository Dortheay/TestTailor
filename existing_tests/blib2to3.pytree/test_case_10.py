import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            base_0 = module_0.Base()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
