import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = -2722
            bytes_0 = b"\xb5\xc6\xd8\x99WH\x92&w'\x81\x85\x04"
            bytes_1 = b'}\xac\x10\xc6\xf3\xa7!'
            dict_0 = {bytes_0: bytes_0, int_0: bytes_1, bytes_0: int_0, int_0: int_0}
            bool_0 = False
            plugin_load_context_0 = module_0.PluginLoadContext()
            jinja2_loader_0 = module_0.Jinja2Loader(int_0, bytes_0, bytes_0, dict_0, bool_0, plugin_load_context_0)
            str_0 = "Y \tb@V'$z9:iN:~\r"
            plugin_load_context_1 = module_0.PluginLoadContext()
            plugin_path_context_0 = module_0.PluginPathContext(jinja2_loader_0, plugin_load_context_1)
            str_1 = '/tmp/tmp.RpkXg1b7Kt/shell_plugins/windows'
            bool_1 = True
            list_0 = [jinja2_loader_0, bool_1, dict_0]
            set_0 = set()
            plugin_path_context_1 = module_0.PluginPathContext(jinja2_loader_0, set_0)
            plugin_path_context_2 = module_0.PluginPathContext(plugin_path_context_1, dict_0)
            str_2 = '}-MwQS51Bmj_CQ)*}n}K'
            bool_2 = False
            list_1 = []
            plugin_loader_0 = module_0.PluginLoader(str_2, plugin_load_context_0, bool_2, str_1, list_1)
            list_2 = [set_0, set_0, bool_0, plugin_path_context_2]
            var_0 = plugin_loader_0.has_plugin(list_2)
            plugin_loader_1 = module_0.PluginLoader(str_1, bytes_1, list_0, plugin_path_context_2, plugin_loader_0, dict_0)
            var_1 = plugin_loader_1.add_directory(str_0, plugin_path_context_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
