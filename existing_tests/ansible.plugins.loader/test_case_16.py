import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            int_0 = 3199
            str_0 = 'k'
            plugin_load_context_0 = module_0.PluginLoadContext()
            list_0 = [str_0]
            str_1 = '^('
            list_1 = [str_0, int_0, plugin_load_context_0]
            tuple_0 = ()
            var_0 = plugin_load_context_0.resolve(list_0, str_1, list_1, tuple_0)
            var_1 = plugin_load_context_0.redirect(str_0)
            dict_0 = {}
            var_2 = module_0.add_all_plugin_dirs(dict_0)
            str_2 = 'h'
            str_3 = '#wN}O42n9$":chdZ<'
            var_3 = module_0.get_shell_plugin(dict_0, str_2)
            list_2 = [var_3, var_3]
            str_4 = ''
            var_4 = plugin_load_context_0.nope(list_2)
            float_0 = 0.5
            plugin_path_context_0 = module_0.PluginPathContext(float_0, float_0)
            int_1 = -654
            tuple_1 = ()
            jinja2_loader_0 = module_0.Jinja2Loader(int_1, tuple_1, dict_0, dict_0)
            plugin_path_context_1 = module_0.PluginPathContext(plugin_path_context_0, jinja2_loader_0)
            bool_0 = False
            var_5 = plugin_load_context_0.nope(bool_0)
            list_3 = [var_3, str_3, str_4]
            var_6 = plugin_load_context_0.record_deprecation(dict_0, list_3, list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
