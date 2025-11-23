import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            plugin_not_found_0 = module_0.PluginNotFound()
            doc_c_l_i_0 = module_0.DocCLI(plugin_not_found_0)
            list_0 = []
            role_mixin_0 = module_0.RoleMixin(*list_0)
            str_0 = 'f>q'
            dict_0 = None
            complex_0 = None
            var_0 = doc_c_l_i_0.format_snippet(str_0, dict_0, complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
