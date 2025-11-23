import unittest
import timeout_decorator
import pymonet.lazy as module_0
import builtins as module_1

class Test_Lazy_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '\n        If Maybe is empty or filterer returns False return default_value, in other case\n        return new instance of Maybe with the same value.\n\n        :param filterer:\n        :type filterer: Function(A) -> Boolean\n        :returns: copy of self when filterer returns True, in other case empty Maybe\n        :rtype: Maybe[A] | Maybe[None]\n        '
        lazy_0 = module_0.Lazy(str_0)
        str_1 = lazy_0.__str__()
        dict_0 = {}
        object_0 = module_1.object(**dict_0)
        bool_0 = lazy_0.__eq__(object_0)
        str_2 = lazy_0.__str__()

if __name__ == "__main__":
    unittest.main()
