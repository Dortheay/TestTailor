import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            tracer_0 = module_0.Tracer()
            str_0 = '2(\ngf@Xn'
            set_0 = set()
            int_0 = 2248
            str_1 = "ez.7/J'|u6*;X:$AF1_2"
            dict_0 = {str_1: set_0}
            var_0 = tracer_0.__enter__()
            dict_1 = {str_0: dict_0, str_0: str_1, tracer_0: str_0}
            tracer_1 = module_0.Tracer(str_0, set_0, int_0, str_1, dict_0, dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
