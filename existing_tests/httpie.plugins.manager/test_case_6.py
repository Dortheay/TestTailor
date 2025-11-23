import unittest
import timeout_decorator
import httpie.plugins.manager as module_0

class Test_Manager_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            plugin_manager_0 = module_0.PluginManager()
            str_0 = '(:v8exp&%>0%#Kv=,I'
            type_0 = plugin_manager_0.get_auth_plugin(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
