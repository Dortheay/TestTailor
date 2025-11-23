import unittest
import timeout_decorator
import thefuck.logs as module_0
import datetime as module_1

class Test_Logs_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = 1519.71
            list_0 = [float_0]
            list_1 = [list_0]
            var_0 = module_0.debug_time(list_1)
            str_0 = '.taz'
            dict_0 = None
            var_1 = module_0.failed(dict_0)
            bool_0 = False
            list_2 = [str_0, bool_0, bool_0]
            set_0 = {str_0}
            float_1 = 0.1
            var_2 = module_0.version(list_2, set_0, float_1)
            int_0 = 1210
            var_3 = module_0.rule_failed(str_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
