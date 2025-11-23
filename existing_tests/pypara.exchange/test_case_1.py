import unittest
import timeout_decorator
import pypara.exchange as module_0

class Test_Exchange_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 1206
            list_0 = [int_0, int_0, int_0, int_0]
            f_x_rate_0 = module_0.FXRate(*list_0)
            f_x_rate_1 = f_x_rate_0.__invert__()
            f_x_rate_service_0 = module_0.FXRateService(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
