import unittest
import timeout_decorator
import httpie.plugins.manager as module_0

class Test_Manager_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            list_0 = [dict_0]
            plugin_manager_0 = module_0.PluginManager(*list_0)
            list_1 = plugin_manager_0.get_auth_plugins()
            bytes_0 = b'\x12\xdf\xa1'
            var_0 = plugin_manager_0.unregister(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
