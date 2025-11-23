import unittest
import timeout_decorator
import sanic.mixins.exceptions as module_0

class Test_Exceptions_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        exception_mixin_0 = module_0.ExceptionMixin()

if __name__ == "__main__":
    unittest.main()
