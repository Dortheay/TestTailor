import unittest
import timeout_decorator
import httpie.context as module_0
import httpie.output.formatters.colors as module_1

class Test_Colors_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'E)/2has~1APb\t*Nq'
            solarized256_style_0 = module_1.Solarized256Style()
            bytes_0 = b'D,Za\xe5E'
            optional_0 = module_1.get_lexer(str_0, bytes_0, bytes_0)
            str_1 = 'K\r/c+'
            bool_0 = True
            optional_1 = module_1.get_lexer(str_1, bool_0)
            environment_0 = module_0.Environment()
            dict_0 = {}
            color_formatter_0 = module_1.ColorFormatter(environment_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
