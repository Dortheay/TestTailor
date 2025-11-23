import unittest
import timeout_decorator
import httpie.output.formatters.colors as module_0
import httpie.context as module_1

class Test_Colors_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = True
        str_0 = 'E)/2has~1APb\t*Nq'
        environment_0 = module_1.Environment()
        solarized256_style_0 = module_0.Solarized256Style()
        optional_0 = module_0.get_lexer(str_0, bool_0)

if __name__ == "__main__":
    unittest.main()
