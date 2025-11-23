import unittest
import timeout_decorator
import typesystem.tokenize.positional_validation as module_0

class Test_Positional_validation_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            token_0 = None
            any_0 = module_0.validate_with_positions(token=token_0, validator=token_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
