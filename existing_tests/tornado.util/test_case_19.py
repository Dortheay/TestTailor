import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        var_0 = module_0.doctests()

if __name__ == "__main__":
    unittest.main()
