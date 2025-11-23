import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = 3215
            str_0 = '~eFP10V~+f>G'
            dict_0 = {str_0: int_0}
            var_0 = module_0.add_all_plugin_dirs(dict_0)
            str_1 = 'R/)Qv\t3zg,?`'
            plugin_load_context_0 = module_0.PluginLoadContext()
            list_0 = [dict_0, dict_0, var_0, plugin_load_context_0]
            plugin_loader_0 = module_0.PluginLoader(str_1, plugin_load_context_0, plugin_load_context_0, list_0)
            str_2 = ';2xw9~ss;O^3P3]\x0c2},/'
            dict_1 = {plugin_loader_0: plugin_load_context_0}
            tuple_0 = None
            list_1 = []
            str_3 = '9\x0cw4Y5.+*%Qz6}{P0Qu~'
            tuple_1 = (dict_1, tuple_0, list_1, str_3)
            plugin_path_context_0 = module_0.PluginPathContext(str_2, tuple_1)
            bytes_0 = b'\x99/\x80\xb6\x0f+hOR\xa0\x9cf'
            tuple_2 = (plugin_path_context_0, bytes_0)
            var_1 = plugin_loader_0.find_plugin(plugin_loader_0, tuple_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
