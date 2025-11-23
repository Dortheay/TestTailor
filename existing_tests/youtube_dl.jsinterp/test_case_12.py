import unittest
import timeout_decorator
import youtube_dl.jsinterp as module_0

class Test_Jsinterp_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '\n    function testFunc(a, b) {\n        return a + b;\n    }\n    '
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        str_1 = 'testFunc'
        var_0 = j_s_interpreter_0.extract_function(str_1)
        var_1 = callable(var_0)

if __name__ == "__main__":
    unittest.main()
