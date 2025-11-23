import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'gIi|-8rA"&'
            str_1 = '=6> +^pD{rZP9lyhkDD'
            j_s_interpreter_0 = module_0.JSInterpreter(str_1)
            var_0 = j_s_interpreter_0.call_function(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
