import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            gitlab_0 = module_0.Gitlab()
            str_0 = gitlab_0.api_url()
            optional_0 = gitlab_0.token()
            optional_1 = gitlab_0.token()
            str_1 = 'Asset upload '
            list_0 = []
            str_2 = 'mP8c'
            str_3 = '(k"/CW%F'
            str_4 = 'H\t\x0c[HV'
            bool_0 = module_0.post_changelog(str_2, str_1, str_3, str_4)
            gitlab_1 = module_0.Gitlab(*list_0)
            str_5 = None
            bool_1 = gitlab_0.check_build_status(str_5, str_5, str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
