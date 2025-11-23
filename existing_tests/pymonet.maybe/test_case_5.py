import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            callable_0 = None
            bool_0 = True
            list_0 = []
            bool_1 = False
            float_0 = -252.9
            maybe_0 = module_0.Maybe(float_0, bool_1)
            var_0 = maybe_0.to_validation()
            maybe_1 = module_0.Maybe(list_0, bool_1)
            var_1 = maybe_1.to_validation()
            var_2 = maybe_1.to_try()
            maybe_2 = module_0.Maybe(bool_0, bool_0)
            var_3 = maybe_2.to_lazy()
            var_4 = maybe_2.bind(callable_0)
            str_0 = '\n        Returns new ImmutableList with only this elements that passed\n        info argument returns True\n\n        :param fn: function to call with ImmutableList value\n        :type fn: Function(A) -> bool\n        :returns: ImmutableList[A]\n        '
            str_1 = 'O;'
            float_1 = 1180.8686
            object_0 = module_1.object()
            var_5 = maybe_1.to_either()
            bool_2 = maybe_1.__eq__(object_0)
            dict_0 = {str_0: callable_0, str_1: str_0, str_1: float_1, str_1: float_1}
            object_1 = module_1.object(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
