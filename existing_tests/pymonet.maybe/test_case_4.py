import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '\n    Maybe type is the most common way of representing nothingness (or the null type).\n    Maybe is effectively abstract and has two concrete subtypes: Box (also Some) and Nothing.\n    '
            bool_0 = False
            maybe_0 = module_0.Maybe(str_0, bool_0)
            var_0 = maybe_0.to_either()
            set_0 = set()
            callable_0 = None
            bool_1 = True
            maybe_1 = module_0.Maybe(set_0, bool_1)
            var_1 = maybe_1.bind(callable_0)
            bool_2 = True
            var_2 = None
            maybe_2 = module_0.Maybe(set_0, bool_2)
            var_3 = maybe_2.map(var_2)
            list_0 = [str_0]
            object_0 = module_1.object(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
