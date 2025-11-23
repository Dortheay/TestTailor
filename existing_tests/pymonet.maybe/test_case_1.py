import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            set_0 = None
            int_0 = -1332
            tuple_0 = ()
            tuple_1 = ()
            bool_0 = False
            maybe_0 = module_0.Maybe(tuple_1, bool_0)
            maybe_1 = module_0.Maybe(maybe_0, bool_0)
            var_0 = maybe_1.get_or_else(tuple_0)
            str_0 = '2hu'
            dict_0 = {str_0: set_0}
            bool_1 = False
            maybe_2 = module_0.Maybe(dict_0, bool_1)
            var_1 = maybe_2.to_box()
            list_0 = [int_0, int_0, int_0]
            bool_2 = False
            maybe_3 = module_0.Maybe(list_0, bool_2)
            var_2 = maybe_3.bind(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
