import unittest
import timeout_decorator
import sanic.mixins.exceptions as module_0

class Test_Exceptions_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bool_0 = False
        exception_mixin_0 = module_0.ExceptionMixin()
        var_0 = exception_mixin_0.exception(apply=bool_0)

if __name__ == "__main__":
    unittest.main()
