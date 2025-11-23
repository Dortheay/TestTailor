import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'N!XA_#{^\x0bbS'
            list_0 = [str_0, str_0, str_0, str_0]
            j_s_interpreter_0 = module_0.JSInterpreter(list_0)
            var_0 = j_s_interpreter_0.interpret_statement(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
