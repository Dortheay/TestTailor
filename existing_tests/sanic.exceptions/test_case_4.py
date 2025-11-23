import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        int_0 = 2611
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
        forbidden_0 = module_0.Forbidden(int_0, dict_0)
        invalid_signal_0 = module_0.InvalidSignal(forbidden_0)

if __name__ == "__main__":
    unittest.main()
