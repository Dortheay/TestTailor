import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            int_0 = 1245
            plugin_load_context_0 = module_0.PluginLoadContext()
            dict_0 = {}
            set_0 = {int_0}
            float_0 = 0.5
            plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, dict_0, set_0, set_0, float_0)
            var_0 = plugin_loader_0.__getstate__()
            var_1 = module_0.get_shell_plugin(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
