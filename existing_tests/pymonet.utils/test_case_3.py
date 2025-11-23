import unittest
import timeout_decorator
import pymonet.utils as module_0

class Test_Utils_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            callable_0 = None
            callable_1 = module_0.memoize(callable_0)
            callable_2 = module_0.memoize(callable_1)
            str_0 = '\n        :returns: Copy of self\n        :rtype: Left[A]\n        '
            list_0 = [callable_1]
            var_0 = module_0.compose(str_0, *list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
