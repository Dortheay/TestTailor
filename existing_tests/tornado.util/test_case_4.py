import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = -3444.69513
            dict_0 = {}
            module_0.exec_in(float_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
