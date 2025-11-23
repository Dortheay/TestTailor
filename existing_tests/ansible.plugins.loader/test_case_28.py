import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        dict_0 = {}
        var_0 = module_0.get_all_plugin_loaders()
        list_0 = [dict_0, dict_0, dict_0]
        str_0 = None
        int_0 = -1149
        float_0 = 2000.232476
        dict_1 = {str_0: float_0}
        bool_0 = False
        jinja2_loader_0 = module_0.Jinja2Loader(str_0, float_0, dict_1, bool_0, str_0)
        set_0 = {float_0}
        plugin_load_context_0 = module_0.PluginLoadContext()
        tuple_0 = (set_0, plugin_load_context_0, set_0)
        str_1 = 'AsD!?HL'
        dict_2 = {str_0: str_0, str_1: str_0, str_0: str_0}
        plugin_loader_0 = module_0.PluginLoader(int_0, jinja2_loader_0, tuple_0, dict_2)
        var_1 = plugin_loader_0.has_plugin(list_0, str_0)

if __name__ == "__main__":
    unittest.main()
