import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        dict_0 = {}
        base_exception_0 = module_1.BaseException(**dict_0)
        optional_0 = module_0.errno_from_exception(base_exception_0)

if __name__ == "__main__":
    unittest.main()
