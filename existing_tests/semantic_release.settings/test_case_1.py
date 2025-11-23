import unittest
import timeout_decorator
import semantic_release.settings as module_0

class Test_Settings_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = module_0.current_changelog_components()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
