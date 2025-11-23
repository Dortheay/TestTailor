import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = -2079
            grammar_0 = module_1.Grammar()
            str_0 = ')oFQ#mp'
            str_1 = 'm<u#Oh>KY@\\'
            int_1 = None
            int_2 = -248
            tuple_0 = (int_1, int_2)
            tuple_1 = (str_1, tuple_0)
            none_type_0 = None
            tuple_2 = (int_0, str_0, tuple_1, none_type_0)
            var_0 = module_0.convert(grammar_0, tuple_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
