import unittest
import timeout_decorator
import youtube_dl.swfinterp as module_0

class Test_Swfinterp_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            dict_0 = {}
            undefined_0 = None
            int_0 = -1760
            float_0 = 1429.162667
            int_1 = -383
            bytes_0 = b''
            a_v_m_class_0 = module_0._AVMClass(int_1, bytes_0, dict_0)
            var_0 = a_v_m_class_0.__repr__()
            a_v_m_class_1 = module_0._AVMClass(int_0, float_0)
            a_v_m_class__object_0 = module_0._AVMClass_Object(a_v_m_class_1)
            var_1 = a_v_m_class_1.__repr__()
            set_0 = {undefined_0, undefined_0, undefined_0}
            s_w_f_interpreter_0 = module_0.SWFInterpreter(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
