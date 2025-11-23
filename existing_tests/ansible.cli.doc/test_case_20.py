import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = ' .wr m#;f!1<&O'
            doc_c_l_i_0 = module_0.DocCLI(str_0)
            str_1 = '6\\Z&Fg&'
            dict_0 = {str_1: str_1, str_1: str_1}
            dict_1 = {}
            list_0 = [str_0, dict_0]
            plugin_not_found_0 = module_0.PluginNotFound()
            var_0 = doc_c_l_i_0.add_fields(dict_0, dict_1, list_0, plugin_not_found_0)
            tuple_0 = ()
            doc_c_l_i_1 = module_0.DocCLI(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
