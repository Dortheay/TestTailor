import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'N!XA_#{^\x0bbS'
            str_1 = ''
            list_0 = [str_1, str_1, str_1]
            j_s_interpreter_0 = module_0.JSInterpreter(list_0)
            float_0 = 771.301
            float_1 = -1709.923513569218
            set_0 = {float_0, str_1, float_1, float_0}
            tuple_0 = (list_0, set_0)
            list_1 = [str_1, float_1]
            var_0 = j_s_interpreter_0.build_function(tuple_0, list_1)
            j_s_interpreter_1 = module_0.JSInterpreter(str_0)
            str_2 = '0kwG{>^~YZw%:QI'
            str_3 = 'LJwN7T_fo W'
            bool_0 = False
            var_1 = j_s_interpreter_0.interpret_statement(str_2, str_3, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
