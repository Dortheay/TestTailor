import unittest
import timeout_decorator
import httpie.cli.argparser as module_0

class Test_Argparser_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        h_t_t_pie_argument_parser_0 = module_0.HTTPieArgumentParser()

if __name__ == "__main__":
    unittest.main()
