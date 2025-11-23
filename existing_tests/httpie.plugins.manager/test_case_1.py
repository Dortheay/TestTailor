import unittest
import timeout_decorator
import httpie.plugins.manager as module_0

class Test_Manager_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        type_0 = None
        plugin_manager_0 = module_0.PluginManager()
        var_0 = plugin_manager_0.__repr__()
        list_0 = [type_0, type_0, type_0]
        plugin_manager_1 = module_0.PluginManager()
        var_1 = plugin_manager_1.register(*list_0)

if __name__ == "__main__":
    unittest.main()
