import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '\n        var x = 5;\n        return x + 10;\n    '
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)

if __name__ == "__main__":
    unittest.main()
