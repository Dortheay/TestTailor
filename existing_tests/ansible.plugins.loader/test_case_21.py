import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            bool_0 = False
            bytes_0 = b'g7\xd8\x89\x15\xf3\xe67\x86\xa5\x1bFS\xe1\x0e'
            float_0 = 512.0
            str_0 = '/tmp/tmp.RpkXg1b7Kt/shell_plugins/windows'
            int_0 = -82
            plugin_path_context_0 = module_0.PluginPathContext(str_0, int_0)
            plugin_load_context_0 = module_0.PluginLoadContext()
            list_0 = [plugin_path_context_0, plugin_path_context_0]
            plugin_loader_0 = module_0.PluginLoader(bytes_0, float_0, plugin_path_context_0, plugin_load_context_0, list_0, list_0)
            var_0 = plugin_loader_0.format_paths(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
