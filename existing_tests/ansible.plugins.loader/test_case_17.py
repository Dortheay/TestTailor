import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            int_0 = 3177
            list_0 = None
            float_0 = -1854.9
            bool_0 = False
            str_0 = '/data/zhuxx/TIARA-study/codamosa/test-apps/ansible/lib/ansible/plugins/doc_fragments/__pycache__/windows'
            dict_0 = {float_0: int_0, int_0: float_0, int_0: bool_0}
            dict_1 = {str_0: str_0}
            plugin_load_context_0 = module_0.PluginLoadContext()
            bool_1 = False
            plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, bool_1, dict_0, list_0)
            var_0 = plugin_loader_0.__setstate__(dict_1)
            plugin_loader_1 = module_0.PluginLoader(float_0, bool_0, str_0, dict_0)
            var_1 = plugin_loader_1.get_with_context(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
