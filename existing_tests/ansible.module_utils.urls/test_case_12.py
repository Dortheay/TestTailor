import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            connection_error_0 = module_0.ConnectionError()
            var_0 = module_0.atexit_remove_file(connection_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
