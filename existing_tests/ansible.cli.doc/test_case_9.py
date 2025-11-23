import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            plugin_not_found_0 = module_0.PluginNotFound()
            str_0 = '\\'
            doc_c_l_i_0 = module_0.DocCLI(str_0)
            doc_c_l_i_1 = module_0.DocCLI(doc_c_l_i_0)
            doc_c_l_i_2 = module_0.DocCLI(doc_c_l_i_1)
            var_0 = doc_c_l_i_2.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
