import unittest
import timeout_decorator
import httpie.plugins.manager as module_0

class Test_Manager_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        plugin_manager_0 = module_0.PluginManager()

if __name__ == "__main__":
    unittest.main()
