import unittest
import timeout_decorator
import pypara.exchange as module_0

class Test_Exchange_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            f_x_rate_service_0 = module_0.FXRateService()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
