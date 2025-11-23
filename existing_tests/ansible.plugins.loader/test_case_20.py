import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            list_0 = None
            bytes_0 = b'\xee\xd6('
            set_0 = {list_0, list_0}
            plugin_load_context_0 = module_0.PluginLoadContext()
            str_0 = ''
            dict_0 = {str_0: list_0}
            plugin_path_context_0 = module_0.PluginPathContext(plugin_load_context_0, dict_0)
            int_0 = 29
            set_1 = None
            bytes_1 = b'c\xe1\x85\xdc\xeb\xc5\xce\x0e\xb1\xc8\x8d\x97\x16p\x1b\x1d\xbfa\xed\x17'
            bool_0 = True
            tuple_0 = (plugin_load_context_0, bytes_1, bool_0)
            plugin_loader_0 = module_0.PluginLoader(plugin_path_context_0, int_0, plugin_load_context_0, set_1, tuple_0)
            bool_1 = False
            tuple_1 = (plugin_loader_0, bool_1)
            jinja2_loader_0 = module_0.Jinja2Loader(list_0, set_0, plugin_path_context_0, int_0, tuple_1)
            var_0 = jinja2_loader_0.find_plugin(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
