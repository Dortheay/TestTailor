import unittest
import timeout_decorator
import httpie.plugins.manager as module_0

class Test_Manager_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        plugin_manager_0 = module_0.PluginManager()
        dict_0 = plugin_manager_0.get_formatters_grouped()

if __name__ == "__main__":
    unittest.main()
