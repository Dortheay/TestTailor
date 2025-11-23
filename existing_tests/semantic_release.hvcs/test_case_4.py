import unittest
import timeout_decorator
import semantic_release.hvcs as module_0

class Test_Hvcs_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        dict_0 = {}
        gitlab_0 = module_0.Gitlab(**dict_0)
        optional_0 = gitlab_0.token()

if __name__ == "__main__":
    unittest.main()
