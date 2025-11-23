import unittest
import timeout_decorator
import youtube_dl.swfinterp as module_0

class Test_Swfinterp_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            undefined_0 = module_0._Undefined()
            int_0 = -569
            var_0 = undefined_0.__bool__()
            s_w_f_interpreter_0 = module_0.SWFInterpreter(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
