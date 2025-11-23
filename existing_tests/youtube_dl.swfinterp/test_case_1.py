import unittest
import timeout_decorator
import youtube_dl.swfinterp as module_0

class Test_Swfinterp_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'X`5p+]2(}{!}\\'
            a_v_m_class__object_0 = module_0._AVMClass_Object(str_0)
            var_0 = a_v_m_class__object_0.__repr__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
