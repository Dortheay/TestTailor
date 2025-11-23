import unittest
import timeout_decorator
import typesystem.composites as module_0
import typesystem.fields as module_1

class Test_Composites_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        never_match_0 = module_0.NeverMatch()

if __name__ == "__main__":
    unittest.main()
