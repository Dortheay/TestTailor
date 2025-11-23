import unittest
import timeout_decorator
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

class Test_Helpers_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        session_0 = module_0.build_requests_session()

if __name__ == "__main__":
    unittest.main()
