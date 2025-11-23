import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            sequence_0 = None
            iterator_0 = module_1.walk_body(sequence_0)
            str_0 = '8B7jI h)Dcs'
            import_0 = module_0.Import()
            bool_0 = True
            str_1 = 'I'
            str_2 = 'D]F'
            dict_0 = {str_1: str_2}
            parser_0 = module_1.Parser(bool_0, dict_0)
            parser_0.imports(str_0, import_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
