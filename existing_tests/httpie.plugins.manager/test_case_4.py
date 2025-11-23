import unittest
import timeout_decorator
import httpie.plugins.manager as module_0

class Test_Manager_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        plugin_manager_0 = module_0.PluginManager()
        plugin_manager_1 = module_0.PluginManager()
        var_0 = plugin_manager_1.load_installed_plugins()
        list_0 = plugin_manager_0.get_converters()
        list_1 = plugin_manager_0.get_transport_plugins()
        plugin_manager_2 = module_0.PluginManager()

if __name__ == "__main__":
    unittest.main()
