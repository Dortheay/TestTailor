import unittest
import timeout_decorator
import httpie.output.formatters.colors as module_0
import httpie.context as module_1

class Test_Colors_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'E)/2has~1APb\t*Nq'
        str_1 = '$_A$(5\x0b'
        str_2 = ")\t$:I3')2E)?t~zG`*"
        solarized256_style_0 = module_0.Solarized256Style()
        str_3 = None
        str_4 = '\n    (default) Data items from the command line are serialized as a JSON object.\n    The Content-Type and Accept headers are set to application/json\n    (if not specified).\n\n    '
        optional_0 = module_0.get_lexer(str_4, solarized256_style_0, solarized256_style_0)
        dict_0 = {str_0: str_3, str_2: str_1}
        simplified_h_t_t_p_lexer_0 = module_0.SimplifiedHTTPLexer(**dict_0)

if __name__ == "__main__":
    unittest.main()
