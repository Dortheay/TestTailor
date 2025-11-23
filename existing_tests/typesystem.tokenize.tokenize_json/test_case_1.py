import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

class Test_Tokenize_json_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x12\x7f\xa6\xa0$L)'
            token_0 = module_0.tokenize_json(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
