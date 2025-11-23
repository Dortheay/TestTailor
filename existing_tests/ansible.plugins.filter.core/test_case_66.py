import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_67(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        str_0 = None
        tuple_0 = ()
        var_0 = module_0.to_uuid(tuple_0)
        dict_0 = {str_0: str_0}
        var_1 = module_0.regex_replace(dict_0)
        dict_1 = None
        var_2 = module_0.quote(dict_1)
        list_0 = [dict_1, dict_1]
        str_1 = 'gmcXwMu#r!1}."'
        var_3 = module_0.path_join(str_1)
        var_4 = module_0.b64decode(list_0)

if __name__ == "__main__":
    unittest.main()
