import unittest
import timeout_decorator
import httpie.cli.argparser as module_0
import httpie.context as module_1

class Test_Argparser_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            set_0 = set()
            environment_0 = module_1.Environment(set_0)
            tuple_0 = None
            h_t_t_pie_argument_parser_0 = module_0.HTTPieArgumentParser()
            namespace_0 = h_t_t_pie_argument_parser_0.parse_args(environment_0, tuple_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
