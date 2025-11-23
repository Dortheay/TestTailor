import unittest
import timeout_decorator
import pymonet.lazy as module_0

class Test_Lazy_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            lazy_0 = module_0.Lazy(dict_0)
            list_0 = [dict_0]
            var_0 = lazy_0.to_maybe(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
