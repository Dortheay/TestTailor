import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            set_0 = set()
            validation_error_0 = module_0.ValidationError(messages=set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
