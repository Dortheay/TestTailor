import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bool_0 = True
        str_0 = '(KVM|kvm|Bochs|SmartDC).*'
        str_1 = 'f>'
        str_2 = '\t`R?WP\x0cz#'
        dict_0 = {str_0: bool_0, str_1: str_0, str_2: bool_0}
        int_0 = -925
        plugin_not_found_0 = module_0.PluginNotFound()
        doc_c_l_i_0 = module_0.DocCLI(plugin_not_found_0)
        var_0 = doc_c_l_i_0.find_plugins(bool_0, dict_0, int_0)

if __name__ == "__main__":
    unittest.main()
