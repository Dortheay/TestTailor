import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

class Test_Tokenize_json_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = "u(@\\,N6JAG'%r+\r"
            any_0 = module_0.validate_json(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
