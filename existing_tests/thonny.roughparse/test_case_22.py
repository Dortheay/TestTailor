import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            bool_0 = False
            rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
            dict_0 = {}
            list_0 = []
            var_0 = rough_parser_0.set_str(list_0)
            bytes_0 = b'8\xea\x07'
            string_translate_pseudo_mapping_0 = module_0.StringTranslatePseudoMapping(dict_0, rough_parser_0)
            var_1 = string_translate_pseudo_mapping_0.get(dict_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
