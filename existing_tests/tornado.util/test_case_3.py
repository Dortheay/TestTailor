import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = "s'"
            any_0 = module_0.import_object(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
