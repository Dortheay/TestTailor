import unittest
import timeout_decorator
import httpie.plugins.manager as module_0

class Test_Manager_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            plugin_manager_0 = module_0.PluginManager()
            var_0 = plugin_manager_0.filter()
            list_0 = plugin_manager_0.get_auth_plugins()
            dict_0 = plugin_manager_0.get_auth_plugin_mapping()
            list_1 = plugin_manager_0.get_auth_plugins()
            list_2 = plugin_manager_0.get_formatters()
            var_1 = plugin_manager_0.load_installed_plugins()
            list_3 = plugin_manager_0.get_converters()
            dict_1 = plugin_manager_0.get_formatters_grouped()
            var_2 = plugin_manager_0.load_installed_plugins()
            dict_2 = plugin_manager_0.get_formatters_grouped()
            type_0 = None
            list_4 = [type_0, type_0, type_0, type_0]
            var_3 = plugin_manager_0.register()
            var_4 = plugin_manager_0.register(*list_4)
            var_5 = plugin_manager_0.__repr__()
            var_6 = plugin_manager_0.unregister(type_0)
            var_7 = plugin_manager_0.filter()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
