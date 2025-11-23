import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = ''
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        str_1 = 'x'
        str_2 = 'y'
        str_3 = 'arr'
        int_0 = -1084
        int_1 = 10
        int_2 = 3
        int_3 = [int_2, int_1, int_2]
        int_4 = {str_1: int_0, str_2: int_1, str_3: int_3}
        str_4 = '5'
        int_5 = 100
        var_0 = j_s_interpreter_0.interpret_expression(str_4, int_4, int_5)
        var_1 = j_s_interpreter_0.interpret_expression(str_1, int_4, int_5)
        str_5 = 'x + y'
        var_2 = j_s_interpreter_0.interpret_expression(str_5, int_4, int_5)
        var_3 = j_s_interpreter_0.interpret_expression(str_3, int_4, int_5)
        var_4 = int_4[str_3]
        str_6 = 'arr.reverse()'
        var_5 = j_s_interpreter_0.interpret_expression(str_6, int_4, int_5)

if __name__ == "__main__":
    unittest.main()
