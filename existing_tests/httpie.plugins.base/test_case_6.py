import unittest
import timeout_decorator
import httpie.plugins.base as module_0

class Test_Base_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            base_plugin_0 = module_0.BasePlugin()
            str_0 = 'n#\\]_1n\n]'
            formatter_plugin_0 = None
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, base_plugin_0: formatter_plugin_0}
            transport_plugin_0 = module_0.TransportPlugin()
            int_0 = -2913
            tuple_0 = (dict_0, transport_plugin_0, int_0)
            int_1 = 10
            converter_plugin_0 = module_0.ConverterPlugin(int_1)
            converter_plugin_1 = module_0.ConverterPlugin(converter_plugin_0)
            var_0 = converter_plugin_1.convert(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
