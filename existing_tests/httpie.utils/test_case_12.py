import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            set_0 = None
            var_0 = module_0.get_content_type(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
