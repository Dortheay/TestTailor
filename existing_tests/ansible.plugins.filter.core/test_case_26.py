import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        try:
            str_0 = 'posix_basic'
            dict_0 = {str_0: str_0}
            var_0 = module_0.subelements(str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
