import unittest
import timeout_decorator
import httpie.context as module_0
import httpie.output.formatters.colors as module_1

class Test_Colors_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'E)/2has~1APb\t*Nq'
            environment_0 = module_0.Environment()
            var_0 = environment_0.__repr__()
            solarized256_style_0 = module_1.Solarized256Style()
            float_0 = -684.947
            optional_0 = module_1.get_lexer(str_0, solarized256_style_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
