import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = ''
            j_s_interpreter_0 = module_0.JSInterpreter(str_0)
            str_1 = 'x'
            str_2 = 'y'
            str_3 = 'arr'
            int_0 = 5
            int_1 = 10
            int_2 = 1
            int_3 = -8
            int_4 = [int_2, int_1, int_3]
            int_5 = {str_1: int_0, str_2: int_1, str_3: int_4}
            int_6 = 100
            var_0 = j_s_interpreter_0.interpret_expression(str_1, int_5, int_6)
            str_4 = 'x + y'
            var_1 = j_s_interpreter_0.interpret_expression(str_4, int_5, int_6)
            str_5 = 'arr[2]'
            var_2 = j_s_interpreter_0.interpret_expression(str_5, int_5, int_6)
            str_6 = '3\n~od9Yd'
            var_3 = j_s_interpreter_0.interpret_expression(str_6, int_5, int_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
