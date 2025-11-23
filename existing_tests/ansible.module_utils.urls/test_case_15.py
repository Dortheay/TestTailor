import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            var_0 = module_0.unix_socket_patch_httpconnection_connect()
            int_0 = -1745
            var_1 = module_0.getpeercert(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
