import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'B3B%alJjtKn"fM:'
            float_0 = -1145.78373
            j_s_interpreter_0 = module_0.JSInterpreter(float_0)
            var_0 = j_s_interpreter_0.extract_function(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
