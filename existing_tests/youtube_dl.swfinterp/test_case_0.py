import unittest
import timeout_decorator
import youtube_dl.swfinterp as module_0

class Test_Swfinterp_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x93\xaa7\xe1'
            s_w_f_interpreter_0 = module_0.SWFInterpreter(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
