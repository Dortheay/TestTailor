import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '!Ug;={7;x'
            list_0 = []
            str_1 = 'M'
            list_1 = [str_0, list_0]
            plugin_not_found_0 = module_0.PluginNotFound(*list_1)
            doc_c_l_i_0 = module_0.DocCLI(plugin_not_found_0)
            var_0 = doc_c_l_i_0.get_all_plugins_of_type(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
