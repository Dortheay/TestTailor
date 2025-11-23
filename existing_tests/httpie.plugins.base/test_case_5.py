import unittest
import timeout_decorator
import httpie.plugins.base as module_0

class Test_Base_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = None
            bool_0 = False
            converter_plugin_0 = module_0.ConverterPlugin(bool_0)
            converter_plugin_1 = module_0.ConverterPlugin(converter_plugin_0)
            auth_plugin_0 = module_0.AuthPlugin()
            var_0 = auth_plugin_0.get_auth(int_0, converter_plugin_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
