import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        plugin_load_context_0 = module_0.PluginLoadContext()

if __name__ == "__main__":
    unittest.main()
