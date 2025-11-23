import unittest
import timeout_decorator
import typesystem.composites as module_0
import typesystem.fields as module_1

class Test_Composites_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        never_match_0 = module_0.NeverMatch()
        not_0 = module_0.Not(never_match_0)
        str_0 = 'test_value'
        any_0 = not_0.validate(str_0)

if __name__ == "__main__":
    unittest.main()
