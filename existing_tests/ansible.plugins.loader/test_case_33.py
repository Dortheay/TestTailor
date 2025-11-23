import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'bomPsRWXc'
        int_0 = None
        str_1 = 'Im'
        bytes_0 = b'\x05\xf1\x07\x90'
        dict_0 = {str_0: str_0, str_1: bytes_0}
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_0.record_deprecation(int_0, dict_0, dict_0)

if __name__ == "__main__":
    unittest.main()
