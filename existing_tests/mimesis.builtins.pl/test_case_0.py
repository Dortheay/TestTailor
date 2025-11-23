import unittest
import timeout_decorator
import mimesis.builtins.pl as module_0

class Test_Pl_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        poland_spec_provider_0 = module_0.PolandSpecProvider()

if __name__ == "__main__":
    unittest.main()
