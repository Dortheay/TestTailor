import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            bytes_0 = b'\xe6F\xea\x9e\x8a4\xd3\xc2\x1d\xc6'
            list_0 = None
            str_0 = 'run_tags'
            doc_c_l_i_0 = module_0.DocCLI(str_0)
            var_0 = doc_c_l_i_0.format_snippet(bytes_0, list_0, str_0)
            dict_0 = None
            set_0 = set()
            list_1 = [set_0, dict_0, set_0, set_0]
            plugin_not_found_0 = module_0.PluginNotFound(*list_1)
            bool_0 = None
            role_mixin_0 = module_0.RoleMixin()
            tuple_0 = (list_1, role_mixin_0)
            tuple_1 = (bool_0, list_1, tuple_0, role_mixin_0)
            set_1 = {role_mixin_0, role_mixin_0}
            dict_1 = {str_0: dict_0, list_0: set_1, plugin_not_found_0: tuple_1}
            var_1 = doc_c_l_i_0.get_man_text(dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
