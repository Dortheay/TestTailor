import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = None
            float_0 = 480.331563
            j_s_interpreter_0 = module_0.JSInterpreter(float_0)
            var_0 = j_s_interpreter_0.call_function(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
