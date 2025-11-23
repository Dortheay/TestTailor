import unittest
import timeout_decorator
import blib2to3.pgen2.pgen as module_0

class Test_Pgen_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '\n\tr8~p\\2G\x0b5}#,,'
            float_0 = -4589.989
            parser_generator_0 = module_0.ParserGenerator(str_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
