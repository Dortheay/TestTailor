import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            plugin_load_context_0 = module_0.PluginLoadContext()
            dict_0 = {}
            var_0 = module_0.add_all_plugin_dirs(dict_0)
            str_0 = 'h'
            str_1 = '#wN}O42n9$":chdZ<'
            var_1 = module_0.get_shell_plugin(dict_0, str_0)
            list_0 = [var_1, var_1]
            str_2 = ''
            int_0 = -654
            tuple_0 = ()
            jinja2_loader_0 = module_0.Jinja2Loader(int_0, tuple_0, dict_0, dict_0)
            bool_0 = False
            var_2 = plugin_load_context_0.nope(bool_0)
            list_1 = [var_1, str_1, str_2]
            var_3 = plugin_load_context_0.record_deprecation(dict_0, list_1, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
