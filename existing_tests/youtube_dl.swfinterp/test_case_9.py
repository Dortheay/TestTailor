import unittest
import timeout_decorator
import youtube_dl.swfinterp as module_0

class Test_Swfinterp_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            undefined_0 = None
            a_v_m_class__object_0 = module_0._AVMClass_Object(undefined_0)
            str_0 = 'qr\rHI$V#'
            bytes_0 = b'\xd5\x8d\xfcw\xb6\xd6\xb5\xe4\xfev\x0e%\x99\x99\xb5'
            str_1 = 'Vr}'
            str_2 = '73.0.3683.55'
            dict_0 = {str_0: bytes_0, str_1: str_1, str_2: str_2, str_2: a_v_m_class__object_0}
            list_0 = [undefined_0, a_v_m_class__object_0]
            a_v_m_class_0 = module_0._AVMClass(list_0, undefined_0)
            var_0 = a_v_m_class_0.register_methods(dict_0)
            undefined_1 = module_0._Undefined()
            var_1 = undefined_1.__bool__()
            float_0 = 3680.59293
            list_1 = [float_0, bytes_0, str_0, float_0]
            a_v_m_class_1 = module_0._AVMClass(float_0, list_1)
            a_v_m_class_2 = module_0._AVMClass(bytes_0, a_v_m_class_1)
            var_2 = a_v_m_class_2.__repr__()
            s_w_f_interpreter_0 = module_0.SWFInterpreter(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
