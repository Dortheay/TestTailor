import unittest
import timeout_decorator
import pymonet.lazy as module_0
import builtins as module_1

class Test_Lazy_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        float_0 = -1061.43162
        lazy_0 = module_0.Lazy(float_0)
        lazy_1 = module_0.Lazy(lazy_0)
        list_0 = [lazy_1, float_0]
        str_0 = '\n        It takes as a parameter function returning another Validation.\n        Function is called with Validation value and returns new Validation with previous value\n        and concated new and old errors.\n\n        :param monad: monad contains function\n        :type monad: Function(A) -> Validation[Any, List[E]]\n        :returns: new validation with stored errors\n        :rtype: Validation[A, List[E]]\n        '
        float_1 = -17.774
        dict_0 = {str_0: float_1, str_0: str_0}
        tuple_0 = (dict_0,)
        lazy_2 = module_0.Lazy(tuple_0)
        var_0 = lazy_2.ap(list_0)

if __name__ == "__main__":
    unittest.main()
