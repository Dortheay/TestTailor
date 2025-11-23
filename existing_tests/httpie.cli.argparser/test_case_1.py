import unittest
import timeout_decorator
import httpie.cli.argparser as module_0
import httpie.context as module_1

class Test_Argparser_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            h_t_t_pie_help_formatter_0 = module_0.HTTPieHelpFormatter()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
