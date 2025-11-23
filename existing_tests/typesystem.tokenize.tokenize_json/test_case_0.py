import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

class Test_Tokenize_json_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            tokenizing_decoder_0 = module_0._TokenizingDecoder(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
