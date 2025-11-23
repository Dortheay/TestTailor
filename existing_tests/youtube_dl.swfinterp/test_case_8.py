import unittest
import timeout_decorator
import youtube_dl.swfinterp as module_0

class Test_Swfinterp_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'Q*3YF"b"#\nU'
            bool_0 = False
            a_v_m_class_0 = module_0._AVMClass(str_0, bool_0)
            var_0 = a_v_m_class_0.make_object()
            str_1 = "j\x0cZF:@\n'9HSU\r*z"
            scope_dict_0 = module_0._ScopeDict(str_1)
            float_0 = 2486.0
            s_w_f_interpreter_0 = module_0.SWFInterpreter(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
