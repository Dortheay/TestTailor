import unittest
import timeout_decorator
import pymonet.lazy as module_0

class Test_Lazy_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '\n        If Maybe is empty or filterer returns False return default_value, in other case\n        return new instance of Maybe with the same value.\n\n        :param filterer:\n        :type filterer: Function(A) -> Boolean\n        :returns: copy of self when filterer returns True, in other case empty Maybe\n        :rtype: Maybe[A] | Maybe[None]\n        '
            lazy_0 = module_0.Lazy(str_0)
            str_1 = lazy_0.__str__()
            list_0 = [str_0]
            var_0 = lazy_0.to_box(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
