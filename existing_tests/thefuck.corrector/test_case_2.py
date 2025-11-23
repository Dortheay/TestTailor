import unittest
import timeout_decorator
import thefuck.corrector as module_0

class Test_Corrector_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.get_rules_import_paths()

if __name__ == "__main__":
    unittest.main()
