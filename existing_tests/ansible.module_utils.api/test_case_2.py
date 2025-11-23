import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            var_0 = module_0.rate_limit_argument_spec()
            var_1 = module_0.basic_auth_argument_spec()
            int_0 = 13
            var_2 = module_0.retry(int_0)
            bool_0 = True
            int_1 = -27
            var_3 = module_0.rate_limit(bool_0, int_1)
            str_0 = '`'
            str_1 = None
            var_4 = module_0.retry_argument_spec(str_1)
            dict_0 = None
            var_5 = module_0.retry(str_0, dict_0)
            var_6 = module_0.rate_limit_argument_spec()
            var_7 = module_0.basic_auth_argument_spec()
            var_8 = module_0.basic_auth_argument_spec()
            list_0 = [var_7, var_7, var_7]
            var_9 = module_0.retry()
            var_10 = module_0.basic_auth_argument_spec(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
