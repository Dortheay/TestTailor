import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_54(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        dict_0 = {}
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_0)
        var_0 = module_0.prepare_multipart(parse_result_dotted_dict_0)
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()

if __name__ == "__main__":
    unittest.main()
