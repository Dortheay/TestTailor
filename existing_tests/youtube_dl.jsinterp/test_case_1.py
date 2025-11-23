import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = "'\nO"
            str_1 = 'S\nz0>U]`Mvt<{$o'
            j_s_interpreter_0 = module_0.JSInterpreter(str_1)
            var_0 = j_s_interpreter_0.extract_object(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
