import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        int_0 = -753
        str_0 = "x[\tV.H\x0c'<^cB\t'"
        bytes_0 = b'\xbf\x94\x01\xb5\xadA\xc8\x07\x1c\xc3m\x1f\xa2~\x89X'
        plugin_path_context_0 = module_0.PluginPathContext(str_0, bytes_0)
        float_0 = 1.0
        str_1 = 'i'
        list_0 = [bytes_0, plugin_path_context_0, str_1, str_1]
        tuple_0 = None
        plugin_loader_0 = module_0.PluginLoader(plugin_path_context_0, float_0, list_0, tuple_0)
        str_2 = ''
        list_1 = []
        var_0 = plugin_loader_0.has_plugin(int_0, list_1)
        bool_0 = False
        set_0 = None
        str_3 = '^QG('
        str_4 = '.o~}\ndYtOp0X'
        dict_0 = {str_3: str_4}
        bool_1 = False
        plugin_loader_1 = module_0.PluginLoader(set_0, dict_0, str_2, list_0, bytes_0, bool_1)
        str_5 = 'T5wo$H*(a6TFo'
        dict_1 = {var_0: bool_0, str_5: plugin_loader_1, bytes_0: float_0, bool_0: bool_1}
        var_1 = plugin_loader_0.has_plugin(str_5, dict_1)

if __name__ == "__main__":
    unittest.main()
