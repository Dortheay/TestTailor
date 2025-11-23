import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            base_error_0 = module_0.BaseError()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
