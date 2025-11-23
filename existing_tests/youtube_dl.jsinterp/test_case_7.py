import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '[O9?*'
            list_0 = [str_0, str_0, str_0]
            j_s_interpreter_0 = module_0.JSInterpreter(list_0)
            list_1 = []
            str_1 = "<'x-U"
            j_s_interpreter_1 = module_0.JSInterpreter(list_1, str_1)
            str_2 = '5^3+'
            var_0 = j_s_interpreter_1.interpret_statement(str_2, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
