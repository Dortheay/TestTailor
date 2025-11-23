import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = '~eFP10V~+f>G'
            get_with_context_result_0 = None
            str_1 = 'NK2eoBZf R6GCde\\J^7'
            plugin_load_context_0 = module_0.PluginLoadContext()
            list_0 = [str_0, str_1, get_with_context_result_0]
            str_2 = '\n.$'
            plugin_loader_0 = module_0.PluginLoader(str_1, plugin_load_context_0, list_0, str_2)
            var_0 = plugin_loader_0.print_paths()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
