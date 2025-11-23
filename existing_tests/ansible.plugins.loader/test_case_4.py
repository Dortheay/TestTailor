import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = -5549
            set_0 = {int_0, int_0, int_0}
            str_0 = '&eRFU^'
            dict_0 = None
            tuple_0 = (str_0, dict_0)
            plugin_load_context_0 = module_0.PluginLoadContext()
            var_0 = plugin_load_context_0.record_deprecation(set_0, set_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
