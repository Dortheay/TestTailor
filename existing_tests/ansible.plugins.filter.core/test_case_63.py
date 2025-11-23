import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_64(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        float_0 = 0.001
        str_0 = ''
        var_0 = module_0.regex_search(float_0, str_0)
        bool_0 = False
        filter_module_0 = module_0.FilterModule()
        list_0 = []
        bytes_0 = b'i\xa2&\xef2\xce/\xa6\xa1\xed\xd9\xaf8u\xb2'
        tuple_0 = (bool_0, filter_module_0, list_0, bytes_0)
        var_1 = module_0.mandatory(tuple_0)
        str_1 = '/f8\ne3_bx=)9rBz7(3'
        var_2 = module_0.randomize_list(str_1)

if __name__ == "__main__":
    unittest.main()
