import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            complex_0 = None
            bool_0 = True
            dict_0 = {bool_0: bool_0, complex_0: bool_0, bool_0: complex_0}
            float_0 = 512.0
            plugin_load_context_0 = module_0.PluginLoadContext()
            plugin_path_context_0 = module_0.PluginPathContext(plugin_load_context_0, complex_0)
            plugin_loader_0 = module_0.PluginLoader(bool_0, dict_0, float_0, plugin_path_context_0)
            str_0 = '0(."@K@-YAlIt-jd[)\x0bV'
            dict_1 = {str_0: plugin_path_context_0}
            list_0 = []
            int_0 = 32
            int_1 = -1800
            str_1 = 'D}94\x0bwz(G)0'
            dict_2 = {str_1: int_1}
            jinja2_loader_0 = module_0.Jinja2Loader(plugin_path_context_0, int_0, int_1, bool_0, plugin_load_context_0, dict_2)
            var_0 = jinja2_loader_0.get(dict_1, *list_0, **dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
