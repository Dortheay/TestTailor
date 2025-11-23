import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            plugin_not_found_0 = module_0.PluginNotFound()
            doc_c_l_i_0 = module_0.DocCLI(plugin_not_found_0)
            var_0 = doc_c_l_i_0.init_parser()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
