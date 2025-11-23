import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            float_0 = None
            int_0 = -2718
            bytes_0 = b"\xb5\xc6\xd8\x99WH\x92&w'\x81\x85\x04"
            bytes_1 = b'}\xac\x10\xc6\xf3\xa7!'
            dict_0 = {bytes_0: bytes_0, int_0: bytes_1, bytes_0: int_0, int_0: int_0}
            bool_0 = False
            plugin_load_context_0 = module_0.PluginLoadContext()
            jinja2_loader_0 = module_0.Jinja2Loader(int_0, bytes_0, bytes_0, dict_0, bool_0, plugin_load_context_0)
            plugin_load_context_1 = module_0.PluginLoadContext()
            plugin_path_context_0 = module_0.PluginPathContext(jinja2_loader_0, plugin_load_context_1)
            str_0 = '/tmp/tmp.RpkXg1b7Kt/shell_plugins/windows'
            set_0 = set()
            plugin_path_context_1 = module_0.PluginPathContext(jinja2_loader_0, set_0)
            plugin_path_context_2 = module_0.PluginPathContext(plugin_path_context_1, dict_0)
            str_1 = '}-MwQS51Bmj_CQ)*}n}K'
            bool_1 = False
            list_0 = []
            plugin_loader_0 = module_0.PluginLoader(str_1, plugin_load_context_0, bool_1, str_0, list_0)
            list_1 = [set_0, set_0, bool_0, plugin_path_context_2]
            var_0 = plugin_loader_0.has_plugin(list_1)
            var_1 = jinja2_loader_0.get(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
