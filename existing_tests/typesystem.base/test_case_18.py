import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '4eke9B!b#pN\nQ515N`h'
            base_error_0 = module_0.BaseError(text=str_0)
            list_0 = base_error_0.messages(add_prefix=str_0)
            base_error_1 = module_0.BaseError()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
