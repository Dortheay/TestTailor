import unittest
import timeout_decorator
import httpie.plugins.manager as module_0

class Test_Manager_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        plugin_manager_0 = module_0.PluginManager()
        var_0 = plugin_manager_0.load_installed_plugins()

if __name__ == "__main__":
    unittest.main()
