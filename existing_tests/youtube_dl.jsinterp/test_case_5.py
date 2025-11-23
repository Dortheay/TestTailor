import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'N!XA_#{^\x0bbS'
            str_1 = ''
            list_0 = [str_1, str_1, str_1]
            j_s_interpreter_0 = module_0.JSInterpreter(list_0)
            float_0 = 771.301
            float_1 = -1677.9793
            var_0 = j_s_interpreter_0.build_function(float_1, str_0)
            j_s_interpreter_1 = module_0.JSInterpreter(j_s_interpreter_0, float_0)
            var_1 = j_s_interpreter_1.interpret_statement(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
