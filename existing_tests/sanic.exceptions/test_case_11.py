import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = -1539.00847
            service_unavailable_0 = module_0.ServiceUnavailable(float_0)
            list_0 = [float_0, float_0, float_0]
            header_not_found_0 = module_0.HeaderNotFound(float_0)
            float_1 = -1129.0
            list_1 = [float_0, float_1, header_not_found_0]
            str_0 = 'fMp5RR[!"G(7XG/\tao'
            unauthorized_0 = module_0.Unauthorized(list_1, str_0, list_0)
            int_0 = 1437
            var_0 = module_0.abort(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
