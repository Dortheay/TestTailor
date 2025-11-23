import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            float_0 = -404.32
            set_0 = {float_0, float_0}
            get_with_context_result_0 = None
            bool_0 = False
            bytes_0 = b'\xc6\xffC\xd2\x05\x0b'
            int_0 = -768
            float_1 = 1703.85
            plugin_loader_0 = module_0.PluginLoader(bool_0, bytes_0, int_0, float_1)
            var_0 = plugin_loader_0.has_plugin(set_0, get_with_context_result_0)
            plugin_load_context_0 = module_0.PluginLoadContext()
            plugin_path_context_0 = module_0.PluginPathContext(set_0, set_0)
            list_0 = [float_0, float_0, bytes_0]
            var_1 = plugin_loader_0.get(plugin_path_context_0, *list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
