import unittest
import timeout_decorator
import pymonet.utils as module_0

class Test_Utils_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'ImmutableList: you can not add any other instace than ImmutableList'
            var_0 = None
            var_1 = module_0.identity(var_0)
            var_2 = module_0.identity(var_1)
            var_3 = module_0.identity(var_2)
            list_0 = [str_0, str_0, var_3]
            var_4 = module_0.fn(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
