import unittest
import timeout_decorator
import pymonet.utils as module_0

class Test_Utils_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '\n        Transform Lazy into Try with constructor_fn result.\n        Try will be successful only when constructor_fn not raise anything.\n\n        :returns: Try with constructor_fn result\n        :rtype: Try[A] | Try[Error]\n        '
            int_0 = -1212
            list_0 = [int_0, str_0]
            var_0 = module_0.pipe(int_0, *list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
