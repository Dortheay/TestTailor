import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            str_0 = 'k'
            plugin_load_context_0 = module_0.PluginLoadContext()
            var_0 = plugin_load_context_0.redirect(str_0)
            dict_0 = {}
            var_1 = module_0.add_all_plugin_dirs(dict_0)
            str_1 = 'DPU%$leXHTG'
            str_2 = '\x0bJw'
            var_2 = plugin_load_context_0.nope(str_2)
            var_3 = module_0.get_shell_plugin(dict_0, str_1)
            var_4 = module_0.get_shell_plugin()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
