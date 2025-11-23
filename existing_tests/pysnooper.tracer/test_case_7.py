import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            list_0 = [dict_0, dict_0]
            str_0 = '{}.x'
            var_0 = module_0.get_write_function(list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
