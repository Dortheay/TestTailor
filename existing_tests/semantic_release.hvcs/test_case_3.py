import unittest
import timeout_decorator
import semantic_release.hvcs as module_0

class Test_Hvcs_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '+Q\ngh'
        github_0 = module_0.Github()
        bool_0 = github_0.check_build_status(str_0, str_0, str_0)

if __name__ == "__main__":
    unittest.main()
