import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            bytes_0 = b'\xe6F\xea\x9e\x8a4\xd3\xc2\x1d\xc6'
            list_0 = None
            str_0 = 'run_tags'
            str_1 = 'module'
            doc_c_l_i_0 = module_0.DocCLI(str_1)
            var_0 = doc_c_l_i_0.format_snippet(bytes_0, list_0, str_0)
            dict_0 = None
            set_0 = set()
            list_1 = [set_0, dict_0, set_0, set_0]
            plugin_not_found_0 = module_0.PluginNotFound(*list_1)
            role_mixin_0 = module_0.RoleMixin()
            tuple_0 = (list_1, role_mixin_0)
            role_mixin_1 = module_0.RoleMixin()
            int_0 = -1144
            var_1 = module_0.add_collection_plugins(int_0, set_0)
            list_2 = [plugin_not_found_0]
            list_3 = [set_0, list_2, plugin_not_found_0, plugin_not_found_0]
            str_2 = "!*^-2hP02h'3pO|"
            doc_c_l_i_1 = module_0.DocCLI(list_1)
            var_2 = doc_c_l_i_1.add_fields(tuple_0, list_2, str_0, list_3, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
