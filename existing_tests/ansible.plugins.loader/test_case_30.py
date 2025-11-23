import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bytes_0 = b'\xba\xacW\xf9\xe1\x14'
        tuple_0 = None
        list_0 = [tuple_0]
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_0.record_deprecation(bytes_0, tuple_0, list_0)

if __name__ == "__main__":
    unittest.main()
