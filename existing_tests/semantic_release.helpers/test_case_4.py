import unittest
import timeout_decorator
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

class Test_Helpers_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = ' G3\n$\t`wx#aa\n1qy'
        str_1 = 'BRI/m<%9pIhKVUik}fE'
        session_0 = module_0.build_requests_session()
        set_0 = {str_0, session_0, str_1}
        dict_0 = {str_0: str_0, str_1: set_0}
        int_0 = 1286
        session_1 = module_0.build_requests_session(dict_0, int_0)

if __name__ == "__main__":
    unittest.main()
