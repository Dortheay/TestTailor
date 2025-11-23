import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'OBd46UYb{RDvx8is'
            list_0 = None
            var_0 = module_0.add_all_plugin_dirs(list_0)
            str_1 = '\tLLAw=6y01]~h)K'
            str_2 = None
            str_3 = 'w%'
            bytes_0 = b'\x12q\x94\n\xb30\x87\x81\x84\xdd'
            tuple_0 = (bytes_0, bytes_0)
            dict_0 = {str_0: str_1, str_2: str_0, str_3: tuple_0}
            plugin_load_context_0 = module_0.PluginLoadContext()
            var_1 = plugin_load_context_0.record_deprecation(str_1, dict_0, str_2)
            plugin_load_context_1 = module_0.PluginLoadContext()
            bool_0 = None
            int_0 = -81
            var_2 = module_0.add_dirs_to_loader(bool_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
