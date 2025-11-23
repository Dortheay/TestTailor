import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            semantic_version_0 = module_0.SemanticVersion()
            var_0 = semantic_version_0.__le__(semantic_version_0)
            var_1 = semantic_version_0.__repr__()
            int_0 = 1733
            numeric_0 = module_0._Numeric(int_0)
            semantic_version_1 = module_0.SemanticVersion()
            list_0 = [var_1, int_0]
            var_2 = numeric_0.__gt__(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
