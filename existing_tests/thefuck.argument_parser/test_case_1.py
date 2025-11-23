import unittest
import timeout_decorator
import thefuck.argument_parser as module_0

class Test_Argument_parser_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'&\x88\xa7\n\x08CR*\x06\x8c\xb2\xe7\x13\x8d\xb7'
        list_0 = [bytes_0]
        parser_0 = module_0.Parser()
        var_0 = parser_0.parse(list_0)
        parser_1 = module_0.Parser()

if __name__ == "__main__":
    unittest.main()
