import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = None
            var_0 = module_0.load_json_preserve_order(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
