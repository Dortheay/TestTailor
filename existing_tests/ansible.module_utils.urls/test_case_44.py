import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_45(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_44(self):
        try:
            list_0 = []
            proxy_error_0 = module_0.ProxyError()
            request_0 = module_0.Request(list_0)
            list_1 = []
            parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(*list_1)
            int_0 = 378
            var_0 = request_0.get(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
