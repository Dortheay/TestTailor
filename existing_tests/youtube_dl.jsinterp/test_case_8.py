import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = ''
            j_s_interpreter_0 = module_0.JSInterpreter(str_0)
            str_1 = ''
            str_2 = 'y'
            int_0 = -1084
            int_1 = 3
            int_2 = [int_1, int_0, int_1]
            int_3 = {str_1: int_0, str_2: int_1, str_2: int_2}
            str_3 = ''
            int_4 = 100
            var_0 = j_s_interpreter_0.interpret_expression(str_3, int_3, int_4)
            var_1 = j_s_interpreter_0.interpret_expression(str_1, int_3, int_4)
            var_2 = j_s_interpreter_0.interpret_expression(str_0, int_3, int_4)
            var_3 = j_s_interpreter_0.interpret_expression(str_3, int_3, int_4)
            var_4 = int_3[str_3]
            str_4 = 'arr.reverse()'
            var_5 = j_s_interpreter_0.interpret_expression(str_4, int_3, int_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
